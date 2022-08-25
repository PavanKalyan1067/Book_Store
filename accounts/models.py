from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self, username, email, password, *args, **kwargs):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email), *args, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, *args, **kwargs):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password, *args, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class Information(models.Model):
    method = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class User(AbstractBaseUser, PermissionsMixin):
    password = models.CharField(max_length=250)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    address = models.TextField(max_length=300, null=False, default='Address')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
