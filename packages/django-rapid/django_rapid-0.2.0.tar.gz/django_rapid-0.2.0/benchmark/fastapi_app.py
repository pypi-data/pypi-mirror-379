"""FastAPI app with same realistic endpoints for benchmarking comparison."""

from typing import List
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import func
import json
from datetime import datetime

app = FastAPI()

# SQLite database setup (same as Django)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy models (equivalent to Django models)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id"))
    published_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    view_count = Column(Integer, default=0)
    is_published = Column(Boolean, default=False)

# Pydantic models for API
class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    age: int
    is_active: bool
    created_at: str
    post_count: int

class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    author: UserSchema
    published_at: str
    view_count: int
    is_published: bool

class CreateUserSchema(BaseModel):
    name: str
    email: str
    age: int
    is_active: bool = True

# Database operations (equivalent to Django ORM)
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

def get_users_from_db(db: Session, limit=100):
    """Get users from database with post count - equivalent to Django ORM query."""
    from sqlalchemy.orm import aliased
    from sqlalchemy import func as sql_func

    # Get users with post counts (equivalent to Django's annotate)
    subquery = db.query(
        Post.author_id,
        sql_func.count(Post.id).label('post_count')
    ).group_by(Post.author_id).subquery()

    users = db.query(
        User,
        subquery.c.post_count
    ).outerjoin(
        subquery, User.id == subquery.c.author_id
    ).filter(
        User.is_active == True
    ).limit(limit).all()

    return [
        UserSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age,
            is_active=user.is_active,
            created_at=user.created_at.isoformat(),
            post_count=post_count or 0
        )
        for user, post_count in users
    ]

def get_posts_from_db(db: Session, limit=100):
    """Get posts from database with author info - equivalent to Django ORM with join."""
    posts = db.query(Post).join(User).limit(limit).all()

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

def create_user_in_db(db: Session, user_data):
    """Create user in database - equivalent to Django ORM create."""
    db_user = User(
        name=user_data.name,
        email=user_data.email,
        age=user_data.age,
        is_active=user_data.is_active
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# FastAPI endpoints - equivalent to Django ORM operations

# 1. Basic list endpoints - real database queries
@app.get('/users/', response_model=List[UserSchema])
def users_list(limit: int = Query(100, description="Number of users to return")):
    db = get_db()
    users = get_users_from_db(db, limit)
    return users

@app.get('/posts/', response_model=List[PostSchema])
def posts_list(limit: int = Query(100, description="Number of posts to return")):
    db = get_db()
    posts = get_posts_from_db(db, limit)
    return posts

# 2. Complex relationship queries
@app.get('/user/{user_id}/posts/', response_model=List[PostSchema])
def user_posts(user_id: int):
    db = get_db()
    posts = db.query(Post).join(User).filter(Post.author_id == user_id).all()

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

# 3. CRUD operations with validation
@app.post('/create-user/', response_model=UserSchema)
def create_user(user: CreateUserSchema):
    db = get_db()
    db_user = create_user_in_db(db, user)

    # Get post count for the response
    post_count = db.query(Post).filter(Post.author_id == db_user.id).count()

    return UserSchema(
        id=db_user.id,
        name=db_user.name,
        email=db_user.email,
        age=db_user.age,
        is_active=db_user.is_active,
        created_at=db_user.created_at.isoformat(),
        post_count=post_count
    )

# 4. Search and filtering
@app.get('/search-users/', response_model=List[UserSchema])
def search_users(q: str = Query("", description="Search query"), limit: int = Query(50, description="Limit results")):
    db = get_db()
    from sqlalchemy import or_

    # Search by name or email (equivalent to Django Q objects)
    users = db.query(User).filter(
        or_(User.name.contains(q), User.email.contains(q))
    ).filter(User.is_active == True).limit(limit).all()

    return [
        UserSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age,
            is_active=user.is_active,
            created_at=user.created_at.isoformat(),
            post_count=0  # Not needed for search results
        )
        for user in users
    ]

# 5. Dashboard/Stats endpoint
@app.get('/dashboard/')
def dashboard_data():
    db = get_db()

    # Real database aggregations (equivalent to Django's count())
    total_users = db.query(User).count()
    active_users = db.query(User).filter(User.is_active == True).count()
    total_posts = db.query(Post).count()
    published_posts = db.query(Post).filter(Post.is_published == True).count()

    # Recent users
    recent_users = db.query(User).order_by(User.created_at.desc()).limit(5).all()
    recent_users_data = [
        UserSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age,
            is_active=user.is_active,
            created_at=user.created_at.isoformat(),
            post_count=0
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

# Pure serialization test - where our msgspec optimizations shine!
@app.get('/large-dict/')
def large_dict_serialization(size: int = Query(1000, description="Size of dict to serialize")):
    """Test pure msgspec serialization performance with pre-computed large dict."""

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

    # Use msgspec directly (no Pydantic overhead)
    import msgspec
    encoder = msgspec.json.Encoder()
    json_data = encoder.encode(large_dict)
    return JSONResponse(content=json.loads(json_data))

# Plain endpoints for reference
@app.get('/users-plain/')
def users_plain(limit: int = Query(100, description="Number of users to return")):
    db = get_db()
    users = get_users_from_db(db, limit)
    return JSONResponse(content={'users': [user.dict() for user in users]})

@app.get('/users-msgspec-direct/')
def users_msgspec_direct(limit: int = Query(100, description="Number of users to return")):
    db = get_db()
    users = get_users_from_db(db, limit)
    import msgspec
    encoder = msgspec.json.Encoder()
    json_data = encoder.encode(users)
    return JSONResponse(content=json.loads(json_data))

# Database setup and seeding
def create_tables():
    """Create database tables (equivalent to Django migrations)."""
    Base.metadata.create_all(bind=engine)

def seed_database():
    """Seed database with test data (equivalent to Django fixtures)."""
    db = SessionLocal()

    # Check if data already exists
    user_count = db.query(User).count()
    if user_count > 0:
        db.close()
        return

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

    db.add_all(users)
    db.commit()

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

    db.add_all(posts)
    db.commit()
    db.close()

    print("✅ Database seeded with 1000 users and 1000 posts")

if __name__ == '__main__':
    import uvicorn
    # Setup database
    create_tables()
    seed_database()
    uvicorn.run(app, host='127.0.0.1', port=8002, log_level='error')
