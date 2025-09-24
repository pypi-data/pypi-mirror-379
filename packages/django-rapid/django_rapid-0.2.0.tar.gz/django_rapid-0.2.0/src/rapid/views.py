"""Class-based views for rapid JSON serialization."""

from typing import Type, TypeVar, Any, List
import msgspec
from django.http import HttpRequest, HttpResponse
from django.views import View
from functools import wraps

from .core import json_response
from .decorators import validate

# Fast utility for struct to dict conversion
def struct_to_dict(data):
    """Convert msgspec.Struct to dict efficiently."""
    # Fast path for msgspec.Struct
    if isinstance(data, msgspec.Struct):
        return {f: getattr(data, f) for f in data.__struct_fields__}
    return data


T = TypeVar('T', bound=msgspec.Struct)


class APIView(View):
    """Base API view with automatic msgspec serialization.

    Features:
    - Methods with @validate decorators get request validation + response serialization
    - Methods without decorators that return dicts/lists are auto-serialized to JSON
    - Methods returning HttpResponse objects work as-is

    Usage examples:

        class UserAPI(APIView):
            @validate(response_schema=List[UserOut])           # Response serialization only
            def get(self, request):
                return User.objects.all()

            @validate(UserIn)                                  # Request validation only (most common)
            def post(self, request):
                # request.validated_data contains UserIn instance
                return User.objects.create(...)

            @validate(UserUpdate, response_schema=UserOut)     # Both validation and serialization
            def put(self, request, user_id):
                # request.validated_data contains UserUpdate instance
                user = User.objects.get(id=user_id)
                # update user...
                return user

            def delete(self, request, user_id):
                User.objects.filter(id=user_id).delete()
                return {"message": "User deleted"}  # Auto-serialized to JSON
    """

    def dispatch(self, request, *args, **kwargs):
        """Override dispatch to auto-serialize dict responses."""
        # Get the view method (get, post, put, etc.)
        handler = getattr(self, request.method.lower())

        # Check if method is decorated with validate
        is_decorated = hasattr(handler, '_is_decorated')

        # Call the handler method
        response = super().dispatch(request, *args, **kwargs)

        # If method is not decorated and returns non-HttpResponse, auto-serialize
        if not is_decorated:
            try:
                # Check if it's already an HttpResponse
                if hasattr(response, 'status_code'):
                    return response
            except AttributeError:
                pass

            # If it's a dict/list/etc., serialize to JSON
            return json_response(response, schema=None)

        return response


class ModelAPIView(APIView):
    """API view for single model instances.
    
    Usage:
        class UserDetailAPI(ModelAPIView):
            model = User

            @validate(response_schema=UserOut)
            def get(self, request, pk):
                return self.get_object()

            @validate(UserUpdate, response_schema=UserOut)
            def put(self, request, pk):
                user = self.get_object()
                # Update with request.validated_data
                return user
    """
    
    model = None
    lookup_field = 'pk'
    lookup_url_kwarg = None
    
    def get_object(self):
        """Get the model instance."""
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        return self.model.objects.get(**filter_kwargs)


class ListAPIView(APIView):
    """API view for listing model instances.
    
    Usage:
        class UserListAPI(ListAPIView):
            model = User

            @validate(response_schema=List[UserOut])
            def get(self, request):
                return self.get_queryset()

            @validate(UserIn)
            def post(self, request):
                return self.perform_create(request.validated_data)
    """
    
    model = None
    queryset = None
    
    def get_queryset(self):
        """Get the queryset for listing."""
        if self.queryset is not None:
            return self.queryset.all()
        if self.model is not None:
            return self.model.objects.all()
        raise NotImplementedError("Define either 'model' or 'queryset' or override 'get_queryset()'")
    
    def perform_create(self, validated_data):
        """Create the model instance from validated data."""
        data_dict = struct_to_dict(validated_data)
        return self.model.objects.create(**data_dict)


class CreateAPIView(APIView):
    """API view for creating model instances.
    
    Usage:
        class UserCreateAPI(CreateAPIView):
            model = User

            @validate(UserIn)
            def post(self, request):
                return self.perform_create(request.validated_data)
    """
    
    model = None
    
    def perform_create(self, validated_data):
        """Create the model instance from validated data."""
        data_dict = struct_to_dict(validated_data)
        return self.model.objects.create(**data_dict)


class UpdateAPIView(ModelAPIView):
    """API view for updating model instances.
    
    Usage:
        class UserUpdateAPI(UpdateAPIView):
            model = User

            @validate(UserUpdate)
            def put(self, request, pk):
                return self.perform_update(self.get_object(), request.validated_data)
    """
    
    def perform_update(self, instance, validated_data):
        """Update the model instance with validated data."""
        data_dict = struct_to_dict(validated_data)
        for key, value in data_dict.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class DetailAPIView(ModelAPIView):
    """Combined detail view supporting GET, PUT, PATCH, DELETE with decorators.
    
    Usage:
        class UserDetailAPI(DetailAPIView):
            model = User

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
    """
    
    def perform_update(self, instance, validated_data):
        """Update the model instance with validated data."""
        data_dict = struct_to_dict(validated_data)
        for key, value in data_dict.items():
            setattr(instance, key, value)
        instance.save()
        return instance
