"""ASGI application for Django benchmark."""

import os
import sys
from pathlib import Path

# Add parent directory to path to import django-rapid
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'benchmark.django_app.settings')

from django.conf import settings
if not settings.configured:
    settings.configure(
        DEBUG=False,
        SECRET_KEY='benchmark-secret-key',
        ALLOWED_HOSTS=['*'],
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
        ],
        MIDDLEWARE=[],
        ROOT_URLCONF='benchmark.urls',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        USE_TZ=True,
    )

import django
django.setup()

# Setup database when Django starts
from django.db import connection
from .models import User, Post

def setup_database():
    """Setup database tables and seed with test data."""
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

# Setup database
setup_database()

# Import the application after Django is configured
from django.core.asgi import get_asgi_application
application = get_asgi_application()
