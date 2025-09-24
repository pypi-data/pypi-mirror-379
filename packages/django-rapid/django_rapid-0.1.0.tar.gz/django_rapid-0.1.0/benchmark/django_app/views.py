"""Real-world benchmark views using django-rapid decorators with actual Django models."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from typing import List
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.db import models
from rapid import validate, Schema
import msgspec

# Real Django Models for realistic benchmarking
class User(models.Model):
    """Real Django User model with relationships."""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return f"{self.name} ({self.email})"

class Post(models.Model):
    """Real Django Post model with relationships."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['author', 'is_published']),
            models.Index(fields=['published_at']),
        ]

# Schemas for serialization
class UserSchema(Schema):
    id: int
    name: str
    email: str
    age: int
    is_active: bool
    created_at: str
    post_count: int  # Computed field

class PostSchema(Schema):
    id: int
    title: str
    content: str
    author: UserSchema  # Nested relationship
    published_at: str
    view_count: int
    is_published: bool

class CreateUserSchema(Schema):
    name: str
    email: str
    age: int
    is_active: bool = True

# Database operations (real-world scenarios)
def get_users_from_db(limit=100):
    """Get users from database with post count - real ORM query."""
    users = User.objects.annotate(
        post_count=models.Count('posts')
    ).filter(is_active=True)[:limit]

    # Convert to schemas with our optimized type encoders
    return [
        UserSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age,
            is_active=user.is_active,
            created_at=user.created_at.isoformat(),
            post_count=user.post_count
        )
        for user in users
    ]

def get_posts_from_db(limit=100):
    """Get posts from database with author info - real ORM query with join."""
    posts = Post.objects.select_related('author')[:limit]

    return [
        PostSchema(
            id=post.id,
            title=post.title,
            content=post.content,
            author=UserSchema(
                id=post.author.id,
                name=post.author.name,
                email=post.author.email,
                age=post.author.age,
                is_active=post.author.is_active,
                created_at=post.author.created_at.isoformat(),
                post_count=0  # Not needed for posts
            ),
            published_at=post.published_at.isoformat(),
            view_count=post.view_count,
            is_published=post.is_published
        )
        for post in posts
    ]

def get_user_with_posts(user_id: int):
    """Get user with their posts - complex query with relationship."""
    try:
        user = User.objects.annotate(post_count=models.Count('posts')).get(id=user_id)
        posts = Post.objects.filter(author=user)[:10]  # Get latest 10 posts

        user_schema = UserSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age,
            is_active=user.is_active,
            created_at=user.created_at.isoformat(),
            post_count=user.post_count
        )

        post_schemas = [
            PostSchema(
                id=post.id,
                title=post.title,
                content=post.content,
                author=user_schema,  # Reference the same user object
                published_at=post.published_at.isoformat(),
                view_count=post.view_count,
                is_published=post.is_published
            )
            for post in posts
        ]

        return {
            'user': user_schema,
            'posts': post_schemas
        }
    except User.DoesNotExist:
        return None

def create_user_from_db(user_data):
    """Create user in database - real database write."""
    user = User.objects.create(
        name=user_data['name'],
        email=user_data['email'],
        age=user_data['age'],
        is_active=user_data.get('is_active', True)
    )
    return user

def setup_database():
    """Setup database tables and seed with test data."""
    from django.core.management import execute_from_command_line
    from django.db import connection

    # Create tables
    with connection.schema_editor() as schema_editor:
        schema_editor.create_model(User)
        schema_editor.create_model(Post)

    # Check if data already exists
    if User.objects.count() > 0:
        return

    print("Seeding database with test data...")

    # Create users
    users = []
    for i in range(1, 1001):  # 1000 users
        user = User(
            name=f"User {i}",
            email=f"user{i}@example.com",
            age=20 + (i % 50),
            is_active=i % 2 == 0
        )
        users.append(user)

    User.objects.bulk_create(users)

    # Create posts
    posts = []
    for i in range(1, 1001):  # 1000 posts
        post = Post(
            title=f"Post Title {i}",
            content=f"This is the content of post {i}. " * 10,
            author_id=(i % 10) + 1,  # Distribute posts among first 10 users
            view_count=i * 100,
            is_published=i % 3 == 0  # About 1/3 published
        )
        posts.append(post)

    Post.objects.bulk_create(posts)

    print("✅ Database seeded with 1000 users and 1000 posts")

# Real-world API endpoints using actual database operations

# 1. Basic list endpoints - real ORM queries
@validate(response_schema=List[UserSchema])
def users_list(request: HttpRequest):
    """Get users with post counts - real database query with annotation."""
    limit = int(request.GET.get('limit', 100))
    return get_users_from_db(limit)

@validate(response_schema=List[PostSchema])
def posts_list(request: HttpRequest):
    """Get posts with author info - real database query with joins."""
    limit = int(request.GET.get('limit', 100))
    return get_posts_from_db(limit)

# 2. Complex relationship queries
@validate(response_schema=dict)
def user_with_posts(request: HttpRequest, user_id: int):
    """Get user with their posts - complex relationship query."""
    return get_user_with_posts(user_id)

@validate(response_schema=List[PostSchema])
def user_posts(request: HttpRequest, user_id: int):
    """Get all posts by a specific user."""
    posts = Post.objects.select_related('author').filter(author_id=user_id)
    return [
        PostSchema(
            id=post.id,
            title=post.title,
            content=post.content,
            author=UserSchema(
                id=post.author.id,
                name=post.author.name,
                email=post.author.email,
                age=post.author.age,
                is_active=post.author.is_active,
                created_at=post.author.created_at.isoformat(),
                post_count=0
            ),
            published_at=post.published_at.isoformat(),
            view_count=post.view_count,
            is_published=post.is_published
        )
        for post in posts
    ]

# 3. CRUD operations
@validate(CreateUserSchema, response_schema=UserSchema)
def create_user(request: HttpRequest):
    """Create user with validation - real database write."""
    user_data = request.validated_data
    user = User.objects.create(
        name=user_data.name,
        email=user_data.email,
        age=user_data.age,
        is_active=user_data.is_active
    )
    return UserSchema(
        id=user.id,
        name=user.name,
        email=user.email,
        age=user.age,
        is_active=user.is_active,
        created_at=user.created_at.isoformat(),
        post_count=0
    )

@validate(response_schema=UserSchema)
def get_user(request: HttpRequest, user_id: int):
    """Get single user - real database lookup."""
    try:
        user = User.objects.annotate(post_count=models.Count('posts')).get(id=user_id)
        return UserSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age,
            is_active=user.is_active,
            created_at=user.created_at.isoformat(),
            post_count=user.post_count
        )
    except User.DoesNotExist:
        from django.http import Http404
        raise Http404("User not found")

# 4. Search and filtering
@validate(response_schema=List[UserSchema])
def search_users(request: HttpRequest):
    """Search users by name or email with real database filtering."""
    query = request.GET.get('q', '')
    limit = int(request.GET.get('limit', 50))

    users = User.objects.filter(
        models.Q(name__icontains=query) |
        models.Q(email__icontains=query)
    ).annotate(
        post_count=models.Count('posts')
    )[:limit]

    return [
        UserSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age,
            is_active=user.is_active,
            created_at=user.created_at.isoformat(),
            post_count=user.post_count
        )
        for user in users
    ]

# 5. Dashboard/Stats endpoint
@validate(response_schema=dict)
def dashboard_data(request: HttpRequest):
    """Get dashboard statistics - multiple queries in one endpoint."""
    # Real database aggregations
    total_users = User.objects.count()
    active_users = User.objects.filter(is_active=True).count()
    total_posts = Post.objects.count()
    published_posts = Post.objects.filter(is_published=True).count()

    # Recent users
    recent_users = User.objects.order_by('-created_at')[:5]
    recent_users_data = [
        UserSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age,
            is_active=user.is_active,
            created_at=user.created_at.isoformat(),
            post_count=0  # Not needed for dashboard
        )
        for user in recent_users
    ]

    return {
        'stats': {
            'total_users': total_users,
            'active_users': active_users,
            'total_posts': total_posts,
            'published_posts': published_posts,
        },
        'recent_users': recent_users_data,
        'generated_at': '2024-01-01T00:00:00Z'
    }

# Simple dict serialization test - where our optimizations shine!
def large_dict_serialization(request: HttpRequest):
    """Test pure msgspec serialization performance with pre-computed large dict."""
    size = int(request.GET.get('size', 1000))

    # Pre-computed large dict (no database overhead, no ORM, no type conversion)
    large_dict = {
        'metadata': {
            'total_items': size,
            'page': 1,
            'per_page': size,
            'generated_at': '2024-01-01T00:00:00Z'
        },
        'data': [
            {
                'id': i,
                'name': f'User {i}',
                'email': f'user{i}@example.com',
                'age': 20 + (i % 50),
                'is_active': i % 2 == 0,
                'tags': [f'tag{j}' for j in range(i % 5)],
                'profile': {
                    'bio': f'This is user {i}\'s bio. ' * (i % 3),
                    'avatar': f'https://example.com/avatar/{i}.jpg',
                    'verified': i % 3 == 0
                },
                'stats': {
                    'posts': i * 10,
                    'followers': i * 5,
                    'following': i * 3,
                    'likes': i * 15
                }
            }
            for i in range(1, size + 1)
        ]
    }

    # Use our optimized msgspec encoder directly (no type conversion overhead)
    from rapid.core import encode
    json_bytes = encode(large_dict)
    return HttpResponse(json_bytes, content_type='application/json')

# Plain endpoints for reference
def users_plain(request: HttpRequest):
    limit = int(request.GET.get('limit', 100))
    users = get_users_from_db(limit)
    return JsonResponse({'users': [user.__dict__ for user in users]})

# Using msgspec directly without decorators
def users_msgspec_direct(request: HttpRequest):
    limit = int(request.GET.get('limit', 100))
    users = get_users_from_db(limit)
    import msgspec
    return HttpResponse(msgspec.json.encode(users), content_type='application/json')
