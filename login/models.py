from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, unique=True, default='username')
    password = models.CharField(max_length=15, default='password')
    phone_number = models.CharField(max_length=15, unique=True, default='phone_number')

