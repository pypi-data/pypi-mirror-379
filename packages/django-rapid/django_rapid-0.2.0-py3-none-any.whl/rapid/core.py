"""Core encoding and decoding functions for rapid serialization."""

from typing import Any, Type, TypeVar, Union, List, Callable, Mapping
import msgspec
from django.db.models import QuerySet, Model
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from functools import partial, lru_cache


T = TypeVar('T', bound=msgspec.Struct)


# Forward reference for model_to_dict
def model_to_dict(model_instance: Model) -> dict[str, Any]:
    """Efficiently convert Django model instance to dict."""
    return {field.name: getattr(model_instance, field.name) for field in model_instance._meta.fields}


# Type encoders for Django-specific types
DJANGO_TYPE_ENCODERS: Mapping[Any, Callable[[Any], Any]] = {
    QuerySet: lambda qs: list(qs.values()) if not hasattr(qs, 'model') else [model_to_dict(obj) for obj in qs],
    Model: model_to_dict,
}

# Cached encoders for specific schemas with size limit to prevent memory leaks
# Using regular dict since msgspec objects don't support weak references
_schema_encoders: dict[Type[T], msgspec.json.Encoder] = {}
_schema_decoders: dict[Type[T], msgspec.json.Decoder] = {}
_MAX_CACHE_SIZE = 256  # Limit cache size

# Global encoders/decoders with hooks (pre-created for performance)
# These are defined after the functions to avoid circular references
_default_encoder = None
_default_decoder = None


@lru_cache(maxsize=128)
def get_schema_fields(schema: Type[T]) -> frozenset[str]:
    """Get cached field names for a schema."""
    if hasattr(schema, '__struct_fields__'):
        return frozenset(schema.__struct_fields__)
    return frozenset()

def default_serializer(value: Any, schema: Type[T] | None = None) -> Any:
    """Transform Django-specific values that msgspec can't handle natively.

    Args:
        value: A value to serialize
        schema: Optional schema for field filtering

    Returns:
        A msgspec-compatible value
    """
    from typing import get_origin, get_args
    
    # Extract inner schema if it's a List type
    inner_schema = schema
    if schema:
        origin = get_origin(schema)
        if origin is list or origin is List:
            args = get_args(schema)
            if args:
                inner_schema = args[0]
    
    # Get schema fields if provided (using cached function)
    schema_fields = get_schema_fields(inner_schema) if inner_schema else frozenset()

    # Handle QuerySets with optional schema filtering
    if isinstance(value, QuerySet):
        if schema_fields:
            # Optimize QuerySet to only fetch needed fields
            optimized_qs = value.only(*schema_fields) if len(schema_fields) < len(get_model_field_names(value.model)) else value
            return [model_to_dict_with_schema(obj, schema_fields) for obj in optimized_qs]
        else:
            return list(value.values())

    # Handle Model instances with optional schema filtering
    elif hasattr(value, '_meta') and hasattr(value._meta, 'fields'):
        if schema_fields:
            return model_to_dict_with_schema(value, schema_fields)
        else:
            return model_to_dict(value)

    # Handle lists of models
    elif isinstance(value, list) and value and hasattr(value[0], '_meta'):
        if schema_fields:
            return [model_to_dict_with_schema(item, schema_fields) for item in value]
        else:
            return [model_to_dict(item) for item in value]

    # Handle dict/list types with schema validation
    elif isinstance(value, dict):
        if inner_schema and hasattr(inner_schema, '__struct_fields__'):
            # Validate dict against schema
            try:
                # Filter dict to only include fields in the schema
                filtered = {k: v for k, v in value.items() if k in inner_schema.__struct_fields__}
                # Validate by constructing the schema
                validated = inner_schema(**filtered)
                # Return only the fields defined in the schema
                result = {field: getattr(validated, field) for field in inner_schema.__struct_fields__}
                return result
            except Exception as e:
                # Raise validation error for invalid response data
                raise ValidationError(f"Response validation failed: {e}")
        return value

    # For other types, let msgspec handle it
    return value


@lru_cache(maxsize=128)
def get_model_field_names(model_class: Type[Model]) -> tuple[str, ...]:
    """Get cached field names for a model class."""
    return tuple(field.name for field in model_class._meta.fields)

def model_to_dict_with_schema(model_instance: Model, schema_fields: frozenset[str]) -> dict[str, Any]:
    """Convert model to dict with schema field filtering."""
    field_names = get_model_field_names(model_instance.__class__)
    return {field_name: getattr(model_instance, field_name)
            for field_name in field_names
            if field_name in schema_fields}


def default_deserializer(target_type: Any, value: Any) -> Any:
    """Transform values during deserialization.

    Args:
        target_type: The expected type
        value: The value to transform

    Returns:
        Transformed value
    """
    # For now, let msgspec handle deserialization natively
    # This can be extended later for custom deserialization needs
    return value


def get_schema_encoder(schema: Type[T] | None = None) -> msgspec.json.Encoder:
    """Get or create cached encoder for a specific schema."""
    if schema is None:
        return _default_encoder

    if schema not in _schema_encoders:
        # Limit cache size by clearing if it gets too large
        if len(_schema_encoders) >= _MAX_CACHE_SIZE:
            _schema_encoders.clear()
        _schema_encoders[schema] = msgspec.json.Encoder(enc_hook=partial(default_serializer, schema=schema))

    return _schema_encoders[schema]


def get_schema_decoder(schema: Type[T]) -> msgspec.json.Decoder:
    """Get or create cached decoder for a specific schema."""
    if schema not in _schema_decoders:
        # Limit cache size by clearing if it gets too large
        if len(_schema_decoders) >= _MAX_CACHE_SIZE:
            _schema_decoders.clear()
        _schema_decoders[schema] = msgspec.json.Decoder(type=schema)

    return _schema_decoders[schema]


def encode(data: Any, schema: Type[T] | None = None) -> bytes:
    """Encode data to JSON bytes using msgspec with optimized type encoders.

    Args:
        data: Data to encode (QuerySet, Model instance, list, dict, etc.)
        schema: Optional msgspec.Struct schema for validation/serialization

    Returns:
        JSON bytes
    """
    # Fast path: already bytes
    if isinstance(data, bytes):
        return data
    
    # Fast path: already a msgspec Struct instance
    if hasattr(data, '__struct_fields__'):
        return msgspec.json.encode(data)
    
    # Fast path: simple types that don't need schema validation
    if schema is None and isinstance(data, (dict, list, str, int, float, bool)) and not isinstance(data, Model):
        return msgspec.json.encode(data)
    
    # Use optimized encoder with schema-aware hooks
    encoder = get_schema_encoder(schema)
    return encoder.encode(data)


def decode(json_bytes: bytes, schema: Type[T]) -> T | list[T]:
    """Decode JSON bytes to Python objects using msgspec with optimized caching.

    Args:
        json_bytes: JSON bytes to decode
        schema: msgspec.Struct schema for validation/deserialization

    Returns:
        Decoded and validated data
    """
    decoder = get_schema_decoder(schema)
    return decoder.decode(json_bytes)


def json_response(data: Any, schema: Type[T] | None = None, **kwargs) -> HttpResponse:
    """Create a Django JsonResponse with msgspec encoding.

    Args:
        data: Data to serialize
        schema: Optional msgspec.Struct schema
        **kwargs: Additional arguments for JsonResponse

    Returns:
        Django HttpResponse with JSON content
    """
    json_bytes = encode(data, schema)
    response = HttpResponse(
        json_bytes,
        content_type='application/json',
        **kwargs
    )
    return response


# Initialize global encoders/decoders after all functions are defined
def _initialize_encoders():
    """Initialize global encoders to avoid circular references."""
    global _default_encoder, _default_decoder
    if _default_encoder is None:
        _default_encoder = msgspec.json.Encoder(enc_hook=default_serializer)
    if _default_decoder is None:
        _default_decoder = msgspec.json.Decoder(dec_hook=default_deserializer)


# Initialize on module import
_initialize_encoders()
