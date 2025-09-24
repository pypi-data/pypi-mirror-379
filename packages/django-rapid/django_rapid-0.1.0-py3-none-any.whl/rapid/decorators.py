"""Decorators for rapid JSON serialization."""

from functools import wraps
from typing import Type, TypeVar, Callable, Any, List, Union
import msgspec
from django.http import HttpRequest

from .core import json_response, get_schema_decoder, get_schema_encoder


T = TypeVar('T', bound=msgspec.Struct)


def validate(
    schema: Type[T] | None = None,
    *,
    request_schema: Type[T] | None = None,
    response_schema: Type[T] | None = None
):
    """Unified decorator for request validation and response serialization.

    Usage:
        @validate(UserIn)                                  # Request validation only (most common)
        def create_user(request):
            user_data = request.validated_data
            return User.objects.create(**user_data)

        @validate(response_schema=UserOut)                 # Response serialization only
        def get_user(request):
            return User.objects.get(id=id)

        @validate(UserIn, response_schema=UserOut)         # Both
        def update_user(request, user_id):
            user_data = request.validated_data
            return updated_user

    Args:
        schema: Optional positional schema for request validation (most natural default)
        request_schema: Optional schema for request validation
        response_schema: Optional schema for response serialization

    Returns:
        Decorated view with validation and/or serialization
    """
    # Handle natural defaults: positional schema = request validation
    if schema is not None and request_schema is None:
        request_schema = schema

    # Get optimized decoder if request schema provided
    decoder = None
    if request_schema:
        decoder = get_schema_decoder(request_schema)

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
                        if not body:
                            request.validated_data = None
                        else:
                            if type(body) is str:
                                body = body.encode('utf-8')
                            validated_data = decoder.decode(body)
                            request.validated_data = validated_data
                except msgspec.ValidationError as e:
                    return json_response({'error': f'Validation error: {str(e)}'}, status=400)
                except AttributeError:
                    pass  # Not a request object
                except Exception as e:
                    return json_response({'error': f'Invalid request data: {str(e)}'}, status=400)

            # Call the view function
            result = view_func(*args, **kwargs)

            # EAFP: Try to check if it's HttpResponse
            try:
                if result.status_code and True:  # Access status_code
                    return result
            except AttributeError:
                pass

            # Serialize response if schema provided
            return json_response(result, response_schema)

        # Mark as decorated
        wrapper._is_decorated = True
        return wrapper
    return decorator
