"""URL configuration for benchmark."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # Pure serialization test - where our msgspec optimizations shine!
    path('large-dict/', views.large_dict_serialization),

    # Real-world Django ORM endpoints
    path('users/', views.users_list),  # Real DB query with annotations
    path('posts/', views.posts_list),  # Real DB query with joins
    path('user/<int:user_id>/', views.get_user),  # Single user lookup
    path('user/<int:user_id>/posts/', views.user_posts),  # User posts with relationships
    path('create-user/', views.create_user),  # Real DB write with validation
    path('search-users/', views.search_users),  # Search with filtering
    path('dashboard/', views.dashboard_data),  # Complex multi-query endpoint

    # Reference endpoints for comparison
    path('users-plain/', views.users_plain),
    path('users-msgspec-direct/', views.users_msgspec_direct),
]
