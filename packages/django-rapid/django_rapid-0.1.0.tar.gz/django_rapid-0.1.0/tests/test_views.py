"""Tests for class-based views with decorators."""

import json as stdlib_json
import pytest
from typing import List
from django.test import TestCase, RequestFactory

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
    
