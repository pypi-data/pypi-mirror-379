"""Django-msgspec: Fast JSON serialization for Django using msgspec."""

from .schemas import Schema
from .core import encode, decode, json_response
from .decorators import validate
from .views import (
    APIView,
    ModelAPIView,
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DetailAPIView,
)

__version__ = "0.2.0"

__all__ = [
    # Core functions
    "encode",
    "decode",
    "json_response",
    # Schema
    "Schema",
    # Decorators
    "validate",
    # Views
    "APIView",
    "ModelAPIView",
    "ListAPIView",
    "CreateAPIView",
    "UpdateAPIView",
]
