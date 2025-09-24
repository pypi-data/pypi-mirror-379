"""Core encoding and decoding functions for rapid serialization."""

from typing import Any, Type, TypeVar, Union, List, Callable, Mapping
import msgspec
from django.db.models import QuerySet, Model
from django.http import HttpResponse, JsonResponse
from functools import partial


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

# Cached encoders for specific schemas
_schema_encoders: dict[Type[T], msgspec.json.Encoder] = {}
_schema_decoders: dict[Type[T], msgspec.json.Decoder] = {}

# Global encoders/decoders with hooks (pre-created for performance)
# These are defined after the functions to avoid circular references
_default_encoder = None
_default_decoder = None


def default_serializer(value: Any, schema: Type[T] | None = None) -> Any:
    """Transform Django-specific values that msgspec can't handle natively.

    Args:
        value: A value to serialize
        schema: Optional schema for field filtering

    Returns:
        A msgspec-compatible value
    """
    # Get schema fields if provided
    schema_fields = set()
    if schema and hasattr(schema, '__struct_fields__'):
        schema_fields = set(schema.__struct_fields__)

    # Handle QuerySets with optional schema filtering
    if isinstance(value, QuerySet):
        if schema_fields:
            return [model_to_dict_with_schema(obj, schema_fields) for obj in value]
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

    # For other types, let msgspec handle it
    return value


def model_to_dict_with_schema(model_instance: Model, schema_fields: set[str]) -> dict[str, Any]:
    """Convert model to dict with schema field filtering."""
    return {field.name: getattr(model_instance, field.name)
            for field in model_instance._meta.fields
            if field.name in schema_fields}


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
        _schema_encoders[schema] = msgspec.json.Encoder(enc_hook=partial(default_serializer, schema=schema))

    return _schema_encoders[schema]


def get_schema_decoder(schema: Type[T]) -> msgspec.json.Decoder:
    """Get or create cached decoder for a specific schema."""
    if schema not in _schema_decoders:
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
