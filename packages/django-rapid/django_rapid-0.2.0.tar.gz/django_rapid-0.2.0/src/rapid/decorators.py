"""Decorators for rapid JSON serialization."""

from functools import wraps, lru_cache
from typing import Type, TypeVar, Callable, Any, List, Union, get_origin, get_args
import msgspec
from django.http import HttpRequest

from .core import json_response, get_schema_decoder, get_schema_encoder


T = TypeVar('T', bound=msgspec.Struct)

# Cache for compiled validators
_compiled_validators: dict[Type[T], tuple] = {}

@lru_cache(maxsize=256)
def get_compiled_validator(schema: Type[T]) -> tuple:
    """Get pre-compiled validator components for a schema."""
    decoder = get_schema_decoder(schema)
    origin = get_origin(schema)
    is_list = origin is list or origin is List
    
    if is_list:
        inner_schema = get_args(schema)[0] if get_args(schema) else None
    else:
        inner_schema = schema
    
    return (decoder, is_list, inner_schema)


def validate(
    schema: Type[T] | None = None,
    *,
    request_schema: Type[T] | None = None,
    response_schema: Type[T] | None = None
):
    """Unified decorator for request validation and response serialization.

    Usage:
        @validate(List[UserOut])                           # Request validation AND response serialization
        def get_users(request):
            return User.objects.all()

        @validate(request_schema=UserIn)                   # Request validation only
        def create_user(request):
            user_data = request.validated_data
            return User.objects.create(**user_data)

        @validate(response_schema=UserOut)                 # Response serialization only
        def get_users(request):
            return User.objects.all()

        @validate(request_schema=UserIn, response_schema=UserOut)  # Both
        def update_user(request, user_id):
            user_data = request.validated_data
            # ... update user ...
            return updated_user

    Args:
        schema: Optional positional schema for request validation AND response serialization
        request_schema: Optional schema for request validation
        response_schema: Optional schema for response serialization

    Returns:
        Decorated view with validation and/or serialization
    """
    # Handle natural defaults: positional schema = request validation AND response serialization
    if schema is not None and request_schema is None:
        request_schema = schema

    # Get optimized decoder if request schema provided
    decoder = None
    if request_schema:
        decoder = get_schema_decoder(request_schema)
    
    # Pre-compute response schema type info
    response_is_list = False
    response_inner_schema = response_schema
    if response_schema:
        origin = get_origin(response_schema)
        response_is_list = origin is list or origin is List
        if response_is_list:
            args = get_args(response_schema)
            response_inner_schema = args[0] if args else None

    def decorator(view_func: Callable) -> Callable:
        @wraps(view_func)
        def wrapper(*args, **kwargs) -> Any:
            # EAFP: Try to access request directly
            request = None
            if args:
                # Try first arg
                try:
                    if args[0].method:  # Access method directly
                        request = args[0]
                except (AttributeError, IndexError):
                    # Try second arg (method call)
                    if len(args) > 1:
                        try:
                            if args[1].method:
                                request = args[1]
                        except AttributeError:
                            pass

            if not request:
                request = kwargs.get('request')

            # Validate request if schema provided
            if decoder and request:
                try:
                    method = request.method
                    if method in ('POST', 'PUT', 'PATCH'):
                        body = request.body
                        # Always try to decode the body if we have a request schema
                        # Handle empty body by treating it as empty JSON object {}
                        if not body:
                            body = b'{}'
                        validated_data = decoder.decode(body)
                        request.validated_data = validated_data
                except msgspec.ValidationError as e:
                    return json_response({'error': f'Validation error: {str(e)}'}, status=422)
                except AttributeError:
                    pass  # Not a request object
                except Exception as e:
                    return json_response({'error': f'Invalid request data: {str(e)}'}, status=400)

            # Call the view function
            result = view_func(*args, **kwargs)

            # Fast path: already an HttpResponse (avoid any processing)
            if hasattr(result, 'status_code'):
                return result
            
            # Validate and serialize response if schema provided
            if response_schema:
                # Fast path: already a validated msgspec Struct
                if hasattr(result, '__struct_fields__'):
                    return json_response(result, response_schema)
                
                try:
                    # Use pre-computed type info
                    if response_is_list:
                        # It's a List[Schema], just pass to json_response which handles it
                        return json_response(result, response_schema)
                    
                    # For dicts, validate with msgspec.convert
                    if isinstance(result, dict):
                        try:
                            # Convert dict to schema instance for validation
                            validated = msgspec.convert(result, response_schema, strict=False)
                            # Pass the validated instance directly
                            return json_response(validated, response_schema)
                        except msgspec.ValidationError as e:
                            return json_response({'error': f'Response validation failed: {str(e)}'}, status=500)
                    
                    # For other types, let json_response handle it
                    return json_response(result, response_schema)
                except Exception as e:
                    return json_response({'error': f'Response validation failed: {str(e)}'}, status=500)
            else:
                # No schema, just serialize
                return json_response(result)

        # Mark as decorated
        wrapper._is_decorated = True
        return wrapper
    return decorator
