"""Test models for rapid tests."""

from django.db import models


class UserModel(models.Model):
    """Test user model."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'tests'
