import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404

from core.abstract.models import AbstractManager, AbstractModel


class UserManager(BaseUserManager, AbstractManager):
    def create_user(self, username, email, password=None, **kwargs):
        if email is None:
            raise ValueError("Users must have an email address")
        if username is None:
            raise ValueError("Users must have a username")
        if password is None:
            raise ValueError("Users must have a password")
        user = self.model(
            username=username, email=self.normalize_email(email), **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **kwargs):
        if password is None:
            raise ValueError("Superusers must have a password")
        if email is None:
            raise ValueError("Superusers must have an email address")
        if username is None:
            raise ValueError("Superusers must have a username")
        user = self.create_user(
            username=username, email=email, password=password, **kwargs
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, AbstractModel):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True)
    banks_liked = models.ManyToManyField(
        "core_bank.Bank", related_name="liked_by"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def like(self, bank):
        return self.banks_liked.add(bank)

    def remove_like(self, bank):
        return self.banks_liked.remove(bank)
    
    def has_liked(self, bank):
        return self.banks_liked.filter(pk=bank.pk).exists()

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
