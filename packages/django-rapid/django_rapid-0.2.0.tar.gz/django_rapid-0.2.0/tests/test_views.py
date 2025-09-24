"""Tests for class-based views and functional APIs with decorators."""

import json as stdlib_json
import pytest
from typing import List
from django.test import TestCase, RequestFactory
from django.http import HttpRequest

from rapid import Schema, validate, APIView
from .models import UserModel


class UserOut(Schema):
    """Output schema for user."""
    id: int
    name: str
    email: str
    age: int


class UserIn(Schema):
    """Input schema for user."""
    name: str
    email: str
    age: int


class UserUpdate(Schema):
    """Update schema for user."""
    name: str | None = None
    email: str | None = None
    age: int | None = None


class TestAPIViewWithDecorators(TestCase):
    """Test APIView with method decorators."""
    
    def setUp(self):
        """Set up test data."""
        self.factory = RequestFactory()
        self.user = UserModel.objects.create(
            name="John Doe",
            email="john@example.com",
            age=30
        )
    
    def test_apiview_with_method_decorators(self):
        """Test APIView with decorators on individual methods."""
        
        class UserAPI(APIView):
            @validate(response_schema=List[UserOut])
            def get(self, request):
                return UserModel.objects.all()

            @validate(UserIn)
            def post(self, request):
                return UserModel.objects.create(
                    name=request.validated_data.name,
                    email=request.validated_data.email,
                    age=request.validated_data.age
                )

            @validate(UserUpdate)
            def put(self, request, user_id):
                user = UserModel.objects.get(id=user_id)
                if request.validated_data.name:
                    user.name = request.validated_data.name
                if request.validated_data.email:
                    user.email = request.validated_data.email
                if request.validated_data.age:
                    user.age = request.validated_data.age
                user.save()
                return user

            def delete(self, request, user_id):
                UserModel.objects.filter(id=user_id).delete()
                return {"message": "User deleted", "id": user_id}
        
        view = UserAPI.as_view()
        
        # Test GET
        request = self.factory.get('/users/')
        response = view(request)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert len(data) == 1
        assert data[0]["name"] == "John Doe"
        
        # Test POST
        request = self.factory.post(
            '/users/',
            data=b'{"name": "Jane Doe", "email": "jane@example.com", "age": 25}',
            content_type='application/json'
        )
        response = view(request)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["name"] == "Jane Doe"
        assert UserModel.objects.filter(name="Jane Doe").exists()
        
        # Test PUT
        request = self.factory.put(
            f'/users/{self.user.id}/',
            data=b'{"name": "John Updated", "email": null, "age": null}',
            content_type='application/json'
        )
        response = view(request, user_id=self.user.id)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["name"] == "John Updated"
        self.user.refresh_from_db()
        assert self.user.name == "John Updated"
        
        # Test DELETE
        request = self.factory.delete(f'/users/{self.user.id}/')
        response = view(request, user_id=self.user.id)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["message"] == "User deleted"
        assert data["id"] == self.user.id
        assert not UserModel.objects.filter(id=self.user.id).exists()


class TestFunctionalAPIs(TestCase):
    """Test functional API views with decorators - organized by functionality."""
    

    def setUp(self):
        """Set up test data."""
        self.factory = RequestFactory()

    # === SUCCESS CASES ===
    def test_functional_api_request_validation_success(self):
        """Test functional API with valid request data."""

        class RequestSchema(Schema):
            message: str
            count: int

        @validate(request_schema=RequestSchema)
        def index(request):
            return {
                "received": request.validated_data.message,
                "count": request.validated_data.count
            }

        request = self.factory.post('/api/', data=b'{"message": "hello", "count": 42}', content_type='application/json')
        response = index(request)

        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["received"] == "hello"
        assert data["count"] == 42

    def test_functional_api_response_serialization_only(self):
        """Test functional API with response serialization only."""

        class ResponseSchema(Schema):
            message: str
            data: dict

        @validate(response_schema=ResponseSchema)
        def index(request):
            return {"message": "success", "data": {"key": "value"}}

        request = self.factory.get('/api/')
        response = index(request)

        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["message"] == "success"
        assert data["data"] == {"key": "value"}

    def test_functional_api_both_schemas(self):
        """Test functional API with both request and response schemas."""

        class RequestSchema(Schema):
            name: str

        class ResponseSchema(Schema):
            message: str

        @validate(RequestSchema, response_schema=ResponseSchema)
        def index(request):
            return {"message": f"Hello {request.validated_data.name}"}

        request = self.factory.post('/api/', data=b'{"name": "world"}', content_type='application/json')
        response = index(request)

        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["message"] == "Hello world"

    # === ERROR CASES ===

    # JSON Parsing Errors (400)
    def test_functional_api_malformed_json(self):
        """Test functional API with malformed JSON - should return 400."""

        class RequestSchema(Schema):
            message: str

        @validate(request_schema=RequestSchema)
        def index(request):
            return {"success": True}

        request = self.factory.post('/api/', data=b'invalid json {', content_type='application/json')
        response = index(request)

        assert response.status_code == 400
        data = stdlib_json.loads(response.content)
        assert "error" in data

    # Schema Validation Errors (422)
    def test_functional_api_missing_required_field(self):
        """Test functional API with missing required field."""

        class RequestSchema(Schema):
            message: str
            count: int

        @validate(request_schema=RequestSchema)
        def index(request):
            return {"success": True}

        request = self.factory.post('/api/', data=b'{"message": "hello"}', content_type='application/json')
        response = index(request)

        assert response.status_code == 422
        data = stdlib_json.loads(response.content)
        assert "error" in data

    def test_functional_api_wrong_field_name(self):
        """Test functional API with wrong field name (typo)."""

        class RequestSchema(Schema):
            message: str

        @validate(request_schema=RequestSchema)
        def index(request):
            return {"success": True}

        request = self.factory.post('/api/', data=b'{"mesage": "hello"}', content_type='application/json')
        response = index(request)

        assert response.status_code == 422
        data = stdlib_json.loads(response.content)
        assert "error" in data

    def test_functional_api_wrong_type(self):
        """Test functional API with wrong data type."""

        class RequestSchema(Schema):
            count: int

        @validate(request_schema=RequestSchema)
        def index(request):
            return {"success": True}

        request = self.factory.post('/api/', data=b'{"count": "not_a_number"}', content_type='application/json')
        response = index(request)

        assert response.status_code == 422
        data = stdlib_json.loads(response.content)
        assert "error" in data

    def test_functional_api_empty_body_required_fields(self):
        """Test functional API with empty body but required fields."""

        class RequestSchema(Schema):
            message: str

        @validate(request_schema=RequestSchema)
        def index(request):
            return {"success": True}

        request = self.factory.post('/api/', data=b'', content_type='application/json')
        response = index(request)

        assert response.status_code == 422
        data = stdlib_json.loads(response.content)
        assert "error" in data

    def test_functional_api_nested_validation_error(self):
        """Test functional API with nested object validation error."""

        class NestedSchema(Schema):
            value: int

        class RequestSchema(Schema):
            message: str
            nested: NestedSchema

        @validate(request_schema=RequestSchema)
        def index(request):
            return {"success": True}

        request = self.factory.post('/api/', data=b'{"message": "test", "nested": {"value": "not_int"}}', content_type='application/json')
        response = index(request)

        assert response.status_code == 422
        data = stdlib_json.loads(response.content)
        assert "error" in data

    def test_functional_api_array_validation_error(self):
        """Test functional API with array validation error."""

        class RequestSchema(Schema):
            items: List[str]

        @validate(request_schema=RequestSchema)
        def index(request):
            return {"success": True}

        request = self.factory.post('/api/', data=b'{"items": ["valid", 123, true]}', content_type='application/json')
        response = index(request)

        assert response.status_code == 422
        data = stdlib_json.loads(response.content)
        assert "error" in data

    # === EDGE CASES ===
    def test_functional_api_optional_fields(self):
        """Test functional API with optional fields."""

        class RequestSchema(Schema):
            message: str = None
            count: int = 0

        @validate(request_schema=RequestSchema)
        def index(request):
            data = request.validated_data
            return {
                "message": data.message,
                "count": data.count
            }

        request = self.factory.post('/api/', data=b'{}', content_type='application/json')
        response = index(request)

        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["message"] is None
        assert data["count"] == 0

    def test_functional_api_extra_fields_allowed(self):
        """Test that extra fields are allowed by default."""

        class RequestSchema(Schema):
            message: str

        @validate(request_schema=RequestSchema)
        def index(request):
            return {"received": request.validated_data.message}

        request = self.factory.post('/api/', data=b'{"message": "hello", "extra": "field", "another": 123}', content_type='application/json')
        response = index(request)

        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["received"] == "hello"

    def test_functional_api_unicode_support(self):
        """Test functional API with unicode characters."""

        class RequestSchema(Schema):
            message: str

        @validate(request_schema=RequestSchema)
        def index(request):
            return {"echo": request.validated_data.message}

        request = self.factory.post('/api/', data=r'{"message": "\ud83d\ude00 \u2705"}'.encode(), content_type='application/json')
        response = index(request)

        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["echo"] == "😀 ✅"

    # === RESPONSE VALIDATION TESTS ===
    def test_response_validation_success(self):
        """Test that response validation passes when data matches schema."""

        class ResponseSchema(Schema):
            message: str
            count: int

        @validate(response_schema=ResponseSchema)
        def index(request):
            return {"message": "hello", "count": 42}

        request = self.factory.get('/api/')
        response = index(request)

        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["message"] == "hello"
        assert data["count"] == 42

    def test_response_validation_missing_field(self):
        """Test that response validation fails when required field is missing."""

        class ResponseSchema(Schema):
            message: str
            count: int

        @validate(response_schema=ResponseSchema)
        def index(request):
            return {"message": "hello"}  # Missing 'count' field

        request = self.factory.get('/api/')
        response = index(request)

        assert response.status_code == 500
        data = stdlib_json.loads(response.content)
        assert "error" in data
        assert "Response validation failed" in data["error"]

    def test_response_validation_wrong_type(self):
        """Test that response validation fails when field has wrong type."""

        class ResponseSchema(Schema):
            message: str
            count: int

        @validate(response_schema=ResponseSchema)
        def index(request):
            return {"message": "hello", "count": "not_a_number"}  # Wrong type

        request = self.factory.get('/api/')
        response = index(request)

        assert response.status_code == 500
        data = stdlib_json.loads(response.content)
        assert "error" in data
        assert "Response validation failed" in data["error"]

    def test_response_validation_extra_fields_filtered(self):
        """Test that response validation filters out extra fields not in schema."""

        class ResponseSchema(Schema):
            message: str

        @validate(response_schema=ResponseSchema)
        def index(request):
            return {"message": "hello", "extra": "field", "another": 123}

        request = self.factory.get('/api/')
        response = index(request)

        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["message"] == "hello"
        assert "extra" not in data
        assert "another" not in data

    def test_response_validation_nested_object(self):
        """Test response validation with nested object."""

        class NestedSchema(Schema):
            value: int

        class ResponseSchema(Schema):
            message: str
            nested: NestedSchema

        @validate(response_schema=ResponseSchema)
        def index(request):
            return {"message": "test", "nested": {"value": 42}}

        request = self.factory.get('/api/')
        response = index(request)

        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["message"] == "test"
        assert data["nested"]["value"] == 42

    def test_response_validation_nested_object_invalid(self):
        """Test response validation fails with invalid nested object."""

        class NestedSchema(Schema):
            value: int

        class ResponseSchema(Schema):
            message: str
            nested: NestedSchema

        @validate(response_schema=ResponseSchema)
        def index(request):
            return {"message": "test", "nested": {"value": "not_int"}}

        request = self.factory.get('/api/')
        response = index(request)

        assert response.status_code == 500
        data = stdlib_json.loads(response.content)
        assert "error" in data
        assert "Response validation failed" in data["error"]

    def test_response_validation_with_optional_fields(self):
        """Test response validation with optional fields."""

        class ResponseSchema(Schema):
            message: str
            count: int | None = None

        @validate(response_schema=ResponseSchema)
        def index(request):
            return {"message": "hello"}  # count is optional

        request = self.factory.get('/api/')
        response = index(request)

        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["message"] == "hello"
        assert data["count"] is None
