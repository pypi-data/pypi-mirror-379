# django-rapid

Fast JSON serialization and validation for Django using msgspec. Provides a simple, FastAPI-like interface for high-performance JSON encoding/decoding with automatic request validation and response serialization.

## Installation

```bash
pip install django-rapid
```

## Quick Start

### Basic Usage with Decorators

```python
from typing import List
from rapid import validate, Schema
from django.contrib.auth.models import User

# Define your schemas
class UserOut(Schema):
    id: int
    username: str
    email: str

class UserIn(Schema):
    username: str
    email: str
    password: str

# Response serialization only
@validate(response_schema=List[UserOut])
def get_users(request):
    return User.objects.all()  # Automatically serialized to JSON

# Request validation and response serialization
@validate(UserIn, response_schema=UserOut)
def create_user(request):
    # request.validated_data contains the validated UserIn instance
    user = User.objects.create_user(
        username=request.validated_data.username,
        email=request.validated_data.email,
        password=request.validated_data.password
    )
    return user  # Automatically serialized to UserOut
```

### Class-Based Views

```python
from typing import List
from rapid import APIView, validate, Schema
from django.contrib.auth.models import User

class UserOut(Schema):
    id: int
    username: str
    email: str

class UserListAPI(APIView):
    @validate(response_schema=List[UserOut])
    def get(self, request):
        return User.objects.all()  # Automatically serialized to JSON
```

### Request Validation

```python
from rapid import validate, Schema
from django.contrib.auth.models import User

class UserIn(Schema):
    username: str
    email: str
    password: str

class UserOut(Schema):
    id: int
    username: str
    email: str

@validate(UserIn, response_schema=UserOut)
def create_user(request):
    # request.validated_data contains the validated UserIn instance
    user = User.objects.create_user(
        username=request.validated_data.username,
        email=request.validated_data.email,
        password=request.validated_data.password
    )
    return user  # Automatically serialized to UserOut
```

### Manual Control

For cases where you need more control:

```python
from rapid import encode, decode

# Manual encoding
users = User.objects.all()
json_bytes = encode(users, UserOut)

# Manual decoding with validation
user_data = decode(request.body, UserIn)
```

## Features

- **Fast**: Uses msgspec for high-performance JSON serialization
- **Simple**: FastAPI-like decorator syntax with automatic request validation
- **Django Native**: Works with QuerySets, Model instances, and Django views
- **Type Safe**: Full type hints and schema validation
- **Flexible**: Use decorators, class-based views, or manual encoding/decoding

## API Reference

### Decorators

- `@validate(response_schema=schema)` - Automatically serialize view responses to JSON
- `@validate(schema)` - Validate request data against a schema
- `@validate(request_schema, response_schema=response_schema)` - Combined request validation and response serialization

### Class-Based Views

- `APIView` - Base view class with automatic serialization for decorated methods
- `ListAPIView` - API view for listing model instances
- `ModelAPIView` - API view for single model instances
- `CreateAPIView` - API view for creating model instances
- `UpdateAPIView` - API view for updating model instances
- `DetailAPIView` - Combined detail view with GET, PUT, PATCH, DELETE support

### Core Functions

- `encode(data, schema)` - Manually encode data to JSON
- `decode(json_bytes, schema)` - Manually decode and validate JSON
- `json_response(data, schema)` - Create Django JsonResponse

## Examples

### Simple REST API

```python
# views.py
from typing import List
from rapid import APIView, validate, Schema
from myapp.models import Product

class ProductSchema(Schema):
    id: int
    name: str
    price: float
    in_stock: bool

class ProductListAPI(APIView):
    @validate(response_schema=List[ProductSchema])
    def get(self, request):
        return Product.objects.filter(in_stock=True)

class ProductDetailAPI(APIView):
    @validate(response_schema=ProductSchema)
    def get(self, request, product_id):
        return Product.objects.get(id=product_id)

    @validate(ProductSchema, response_schema=ProductSchema)
    def put(self, request, product_id):
        # Update product with validated data
        product = Product.objects.get(id=product_id)
        for key, value in request.validated_data.__dict__.items():
            setattr(product, key, value)
        product.save()
        return product

# urls.py
urlpatterns = [
    path('products/', ProductListAPI.as_view()),
    path('products/<int:product_id>/', ProductDetailAPI.as_view()),
]
```

### CRUD Operations

```python
from typing import List
from rapid import ListAPIView, CreateAPIView, UpdateAPIView, validate, Schema
from myapp.models import Article

class ArticleIn(Schema):
    title: str
    content: str
    published: bool = False

class ArticleOut(Schema):
    id: int
    title: str
    content: str
    published: bool
    created_at: str

class ArticleList(ListAPIView):
    model = Article

    @validate(response_schema=List[ArticleOut])
    def get(self, request):
        return self.get_queryset()

class ArticleCreate(CreateAPIView):
    model = Article

    @validate(ArticleIn, response_schema=ArticleOut)
    def post(self, request):
        return self.perform_create(request.validated_data)

class ArticleUpdate(UpdateAPIView):
    model = Article

    @validate(ArticleIn, response_schema=ArticleOut)
    def put(self, request, pk):
        return self.perform_update(self.get_object(), request.validated_data)
```

## Performance

django-rapid uses msgspec for JSON operations, providing:

- 3-10x faster serialization than Django's built-in JSON encoder
- 2-5x faster than Django REST Framework
- Lower memory usage
- Automatic validation with better error messages

## Requirements

- Python 3.12+
- Django 5.2+
- msgspec 0.18+

## License

MIT
