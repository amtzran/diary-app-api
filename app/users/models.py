import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, name, first_name, password=None, **extra_fields):
        user = self.model(username=username, name=name, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, name, first_name, password):
        """Create and return a new superuser."""
        user = self.create_user(username, name, first_name, password)
        user.is_staff = True
        user.is_active = True
        user.is_verified = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'first_name']
