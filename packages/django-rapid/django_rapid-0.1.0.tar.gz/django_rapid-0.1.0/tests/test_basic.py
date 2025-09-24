"""Basic tests for rapid functionality."""

import json as stdlib_json
import pytest
from typing import List
from django.test import TestCase, RequestFactory
from django.http import HttpResponse

from rapid import (
    Schema, validate, encode, decode, APIView,
    ModelAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DetailAPIView
)
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


class UserPatch(Schema):
    """Patch schema for user."""
    name: str | None = None


class TestCore(TestCase):
    """Test core encoding/decoding functions."""
    
    def setUp(self):
        """Set up test data."""
        self.user = UserModel.objects.create(
            name="John Doe",
            email="john@example.com",
            age=30
        )
    
    def test_encode_model_instance_with_schema(self):
        """Test encoding a model instance with schema."""
        json_bytes = encode(self.user, UserOut)
        data = stdlib_json.loads(json_bytes)
        
        assert data["id"] == self.user.id
        assert data["name"] == "John Doe"
        assert data["email"] == "john@example.com"
        assert data["age"] == 30
    
    def test_encode_model_instance_without_schema(self):
        """Test encoding a model instance without schema."""
        json_bytes = encode(self.user)
        data = stdlib_json.loads(json_bytes)
        
        assert data["id"] == self.user.id
        assert data["name"] == "John Doe"
        assert data["is_active"] is True
    
    def test_encode_queryset_with_schema(self):
        """Test encoding a queryset with schema."""
        UserModel.objects.create(name="Jane Doe", email="jane@example.com", age=25)

        json_bytes = encode(UserModel.objects.all(), UserOut)
        data = stdlib_json.loads(json_bytes)
        
        assert len(data) == 2
        assert data[0]["name"] == "John Doe"
        assert data[1]["name"] == "Jane Doe"
    
    def test_encode_queryset_without_schema(self):
        """Test encoding a queryset without schema."""
        json_bytes = encode(UserModel.objects.all())
        data = stdlib_json.loads(json_bytes)

        assert len(data) == 1
        assert data[0]["name"] == "John Doe"
    
    def test_decode_with_schema(self):
        """Test decoding with schema validation."""
        json_data = b'{"name": "Alice", "email": "alice@example.com", "age": 28}'
        user = decode(json_data, UserIn)
        
        assert user.name == "Alice"
        assert user.email == "alice@example.com"
        assert user.age == 28


class TestDecorators(TestCase):
    """Test decorator functionality."""
    
    def setUp(self):
        """Set up test data."""
        self.factory = RequestFactory()
        UserModel.objects.create(
            name="John Doe",
            email="john@example.com",
            age=30
        )
    
    def test_validate_decorator_response_only(self):
        """Test @validate decorator for response serialization only."""
        @validate(response_schema=List[UserOut])
        def get_users(request):
            return UserModel.objects.all()

        request = self.factory.get('/users/')
        response = get_users(request)
        
        assert isinstance(response, HttpResponse)
        assert response['Content-Type'] == 'application/json'
        
        data = stdlib_json.loads(response.content)
        assert len(data) == 1
        assert data[0]["name"] == "John Doe"
    
    def test_validate_decorator_without_schema(self):
        """Test @validate decorator without schema."""
        @validate()
        def get_data(request):
            return {"message": "Hello World"}
        
        request = self.factory.get('/data/')
        response = get_data(request)
        
        data = stdlib_json.loads(response.content)
        assert data["message"] == "Hello World"
    
    def test_validate_decorator_request_only(self):
        """Test @validate decorator for request validation only."""
        @validate(UserIn)
        def create_user(request):
            assert hasattr(request, 'validated_data')
            return HttpResponse("Created")
        
        request = self.factory.post(
            '/users/',
            data=b'{"name": "Alice", "email": "alice@example.com", "age": 28}',
            content_type='application/json'
        )
        response = create_user(request)
        
        assert response.status_code == 200
        assert response.content == b"Created"
    
    def test_validate_decorator_invalid_data(self):
        """Test @validate decorator with invalid data."""
        @validate(UserIn)
        def create_user(request):
            return HttpResponse("Created")
        
        request = self.factory.post(
            '/users/',
            data=b'{"name": "Alice"}',  # Missing required fields
            content_type='application/json'
        )
        response = create_user(request)
        
        assert response.status_code == 400
        data = stdlib_json.loads(response.content)
        assert "error" in data
    
    def test_validate_decorator_both_schemas(self):
        """Test @validate decorator with both request and response schemas."""
        @validate(UserIn, response_schema=UserOut)
        def create_user(request):
            assert hasattr(request, 'validated_data')
            user_data = request.validated_data
            user = UserModel.objects.create(
                name=user_data.name,
                email=user_data.email,
                age=user_data.age
            )
            return user

        request = self.factory.post(
            '/users/',
            data=b'{"name": "Bob", "email": "bob@example.com", "age": 35}',
            content_type='application/json'
        )
        response = create_user(request)

        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["name"] == "Bob"
        assert data["email"] == "bob@example.com"

    def test_automatic_json_serialization(self):
        """Test that undecorated methods are automatically serialized to JSON."""
        class TestView(APIView):
            def get(self, request):
                return {"message": "Hello", "data": [1, 2, 3]}

            def post(self, request):
                # Return non-dict to test it's not auto-serialized
                from django.http import HttpResponse
                return HttpResponse("Raw response", content_type='text/plain')

        view = TestView.as_view()

        # Test automatic serialization
        request = self.factory.get('/test/')
        response = view(request)
        assert response.status_code == 200
        assert response['Content-Type'] == 'application/json'
        data = stdlib_json.loads(response.content)
        assert data["message"] == "Hello"
        assert data["data"] == [1, 2, 3]

        # Test HttpResponse is returned as-is
        request = self.factory.post('/test/')
        response = view(request)
        assert response.status_code == 200
        assert response['Content-Type'] == 'text/plain'
        assert response.content == b"Raw response"


class TestViews(TestCase):
    """Test class-based views."""
    
    def setUp(self):
        """Set up test data."""
        self.factory = RequestFactory()
        self.user = UserModel.objects.create(
            name="John Doe",
            email="john@example.com",
            age=30
        )
    
    def test_api_view_with_decorators(self):
        """Test APIView with method decorators."""
        class UserListView(APIView):
            @validate(response_schema=List[UserOut])
            def get(self, request):
                return UserModel.objects.all()

            @validate(UserIn)
            def post(self, request):
                user_data = request.validated_data
                user = UserModel.objects.create(
                    name=user_data.name,
                    email=user_data.email,
                    age=user_data.age
                )
                return user
        
        view = UserListView.as_view()
        
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
            data='{"name": "Alice", "email": "alice@example.com", "age": 28}',
            content_type='application/json'
        )
        response = view(request)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["name"] == "Alice"
        assert UserModel.objects.filter(name="Alice").exists()


class TestClassBasedViews(TestCase):
    """Test all class-based views with the new consolidated decorator API."""

    def setUp(self):
        """Set up test data."""
        self.factory = RequestFactory()
        self.user = UserModel.objects.create(
            name="John Doe",
            email="john@example.com",
            age=30
        )

    def test_model_apiview(self):
        """Test ModelAPIView with natural decorator API."""

        class UserDetailAPI(ModelAPIView):
            model = UserModel

            @validate(response_schema=UserOut)
            def get(self, request, pk):
                return self.get_object()

            @validate(UserUpdate)
            def put(self, request, pk):
                user = self.get_object()
                if request.validated_data.name:
                    user.name = request.validated_data.name
                if request.validated_data.email:
                    user.email = request.validated_data.email
                if request.validated_data.age:
                    user.age = request.validated_data.age
                user.save()
                return user

        view = UserDetailAPI.as_view()

        # Test GET with response serialization
        request = self.factory.get(f'/users/{self.user.id}/')
        response = view(request, pk=self.user.id)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["name"] == "John Doe"

        # Test PUT with request validation
        request = self.factory.put(
            f'/users/{self.user.id}/',
            data='{"name": "John Updated", "email": "johnupdated@example.com", "age": 35}',
            content_type='application/json'
        )
        response = view(request, pk=self.user.id)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["name"] == "John Updated"
        self.user.refresh_from_db()
        assert self.user.name == "John Updated"

    def test_list_apiview(self):
        """Test ListAPIView with natural decorator API."""

        class UserListAPI(ListAPIView):
            model = UserModel

            @validate(response_schema=List[UserOut])
            def get(self, request):
                return self.get_queryset()

            @validate(UserIn)
            def post(self, request):
                return self.perform_create(request.validated_data)

        view = UserListAPI.as_view()

        # Test GET with response serialization
        request = self.factory.get('/users/')
        response = view(request)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert len(data) == 1
        assert data[0]["name"] == "John Doe"

        # Test POST with request validation
        request = self.factory.post(
            '/users/',
            data='{"name": "Jane Doe", "email": "jane@example.com", "age": 25}',
            content_type='application/json'
        )
        response = view(request)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["name"] == "Jane Doe"
        assert UserModel.objects.filter(name="Jane Doe").exists()

    def test_create_apiview(self):
        """Test CreateAPIView with natural decorator API."""

        class UserCreateAPI(CreateAPIView):
            model = UserModel

            @validate(UserIn)
            def post(self, request):
                return self.perform_create(request.validated_data)

        view = UserCreateAPI.as_view()

        # Test POST with request validation
        request = self.factory.post(
            '/users/',
            data='{"name": "Bob Smith", "email": "bob@example.com", "age": 35}',
            content_type='application/json'
        )
        response = view(request)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["name"] == "Bob Smith"
        assert UserModel.objects.filter(name="Bob Smith").exists()

    def test_update_apiview(self):
        """Test UpdateAPIView with natural decorator API."""

        class UserUpdateAPI(UpdateAPIView):
            model = UserModel

            @validate(UserUpdate)
            def put(self, request, pk):
                return self.perform_update(self.get_object(), request.validated_data)

        view = UserUpdateAPI.as_view()

        # Test PUT with request validation
        request = self.factory.put(
            f'/users/{self.user.id}/',
            data='{"name": "John Updated", "email": "johnupdated@example.com", "age": 35}',
            content_type='application/json'
        )
        response = view(request, pk=self.user.id)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["name"] == "John Updated"
        self.user.refresh_from_db()
        assert self.user.name == "John Updated"

    def test_detail_apiview(self):
        """Test DetailAPIView with natural decorator API."""

        class UserDetailAPI(DetailAPIView):
            model = UserModel

            @validate(response_schema=UserOut)
            def get(self, request, pk):
                return self.get_object()

            @validate(UserUpdate)
            def put(self, request, pk):
                return self.perform_update(self.get_object(), request.validated_data)

            @validate(UserPatch)
            def patch(self, request, pk):
                return self.perform_update(self.get_object(), request.validated_data)

            def delete(self, request, pk):
                self.get_object().delete()
                return {"message": "Deleted successfully"}

        view = UserDetailAPI.as_view()

        # Test GET with response serialization
        request = self.factory.get(f'/users/{self.user.id}/')
        response = view(request, pk=self.user.id)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["name"] == "John Doe"

        # Test PUT with request validation
        request = self.factory.put(
            f'/users/{self.user.id}/',
            data='{"name": "John PUT", "email": "johnput@example.com", "age": 35}',
            content_type='application/json'
        )
        response = view(request, pk=self.user.id)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["name"] == "John PUT"

        # Test PATCH with request validation
        request = self.factory.patch(
            f'/users/{self.user.id}/',
            data='{"name": "John PATCH"}',
            content_type='application/json'
        )
        response = view(request, pk=self.user.id)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["name"] == "John PATCH"

        # Test DELETE with automatic serialization
        request = self.factory.delete(f'/users/{self.user.id}/')
        response = view(request, pk=self.user.id)
        assert response.status_code == 200
        data = stdlib_json.loads(response.content)
        assert data["message"] == "Deleted successfully"
        assert not UserModel.objects.filter(id=self.user.id).exists()
