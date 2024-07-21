# backend/authentication/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    dob = models.DateField(null=True, blank=True)
    createAt = models.CharField(max_length=50)
    modifiedAt = models.CharField(max_length=50)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='authentication_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='authentication_users_permissions',
        blank=True
    )

class Admin(models.Model):
    adminId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    lastLogin = models.CharField(max_length=50)
    createAt = models.CharField(max_length=50)
    modifiedAt = models.CharField(max_length=50)

class Login(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    security_question_id = models.CharField(max_length=20, null=True, blank=True)
    answer = models.CharField(max_length=50, null=True, blank=True)
