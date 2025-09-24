"""Base Schema class for rapid serialization."""

import msgspec


class Schema(msgspec.Struct):
    """Base schema class that extends msgspec.Struct.
    
    All schemas should inherit from this class to enable
    automatic serialization with rapid decorators and views.
    """
    pass