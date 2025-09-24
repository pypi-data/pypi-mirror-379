# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `django-rapid`, a Django package that provides high-performance JSON serialization using msgspec with a FastAPI-like decorator syntax. The package is distributed under the name `django-rapid` but imports as `rapid`.

## Commands

### Testing

- `just test` - Run all tests with verbose output
- `just quick` - Run tests quickly without verbose output
- `just test-specific <pattern>` - Run specific test matching pattern (e.g., `just test-specific test_json_decorator`)
- `just test-cov` - Run tests with coverage report
- `just watch` - Watch and rerun tests on file changes

### Development

- `just install` - Install all dependencies including dev dependencies
- `just dev` - Install package in editable mode
- `just lint` - Run ruff linting on src/ and tests/
- `just format` - Auto-format code with ruff
- `just typecheck` - Run mypy type checking
- `just build` - Build the package distribution
- `just clean` - Remove all build artifacts and caches

### Debugging

- `just shell` - Open Django shell with the package loaded

## Architecture

### Core Design Principles

1. **Decorator-Based API**: All serialization/validation is done through decorators (`@json`, `@validate`, `@api`) that work on both functions and class methods.

2. **Type Hint Integration**: Uses Python's `typing.List[Schema]` for collections, not `list[Schema]`. The core `encode()` function detects `List` type hints using `get_origin()` and `get_args()` to extract the inner schema type.

3. **No Backwards Compatibility**: The package explicitly avoids backwards compatibility patterns. Class-level schemas on APIView are removed - only decorator-based approach is supported.

### Key Components

#### Schemas (`src/rapid/schemas.py`)

- `Schema` class extends `msgspec.Struct`
- All user schemas inherit from this base class

#### Core Serialization (`src/rapid/core.py`)

- `encode(data, schema)` - Handles Django QuerySets, Model instances, and lists
  - Detects `List[Schema]` vs `Schema` type hints
  - Automatically extracts model fields matching schema fields
  - Optimized with caching for field lookups
- `decode(json_bytes, schema)` - Deserializes and validates JSON
- `json_response(data, schema)` - Creates Django HttpResponse with msgspec encoding

#### Decorators (`src/rapid/decorators.py`)

- Decorators detect if they're applied to functions vs methods by checking if first arg is `HttpRequest`
- `@json(schema)` - Response serialization only
- `@validate(schema)` - Request validation only
- `@api(request_schema, response_schema)` - Combined validation and serialization
- All decorators set `_is_decorated` flag to prevent double processing

#### Views (`src/rapid/views.py`)

- `APIView` - Base class, requires decorators on methods (no class-level schemas)
- Helper classes: `ListAPIView`, `CreateAPIView`, `UpdateAPIView`, `DetailAPIView`
- `perform_create()` and `perform_update()` convert msgspec Structs to dicts for Django ORM

### Testing Structure

- Tests in `tests/` use a `TestUser` model defined in `tests/models.py`
- Test settings in `tests/settings.py` use in-memory SQLite
- Tests must set `PYTHONPATH=.:src` and `DJANGO_SETTINGS_MODULE=tests.settings`

### Important Implementation Details

1. **List Type Handling**: When a schema is `List[UserOut]`, the code extracts the inner type and applies it to each item in collections. Single instances fail if given a List schema.

2. **Field Filtering**: When converting Django models to schemas, only fields that exist in both the model and schema are included (intersection).

3. **Request Detection**: Decorators determine if they're on a method vs function by checking `isinstance(args[0], HttpRequest)` vs `isinstance(args[1], HttpRequest)`.

4. **Performance**: Recent optimizations include caching decoders, encoders, and field lookups using weakref dictionaries.

## Common Issues

1. **Import Name**: Package installs as `django-rapid` but imports as `rapid` (not `dj_msgspec` or `django_msgspec`)

2. **Type Hints**: Must use `from typing import List` and `List[Schema]`, not Python 3.9+ `list[Schema]`

3. **Test Warnings**: The `TestUser` model triggers pytest collection warnings - this is expected and can be ignored

4. **Empty Request Body**: The decorators handle empty request bodies by setting `request.validated_data = None`
