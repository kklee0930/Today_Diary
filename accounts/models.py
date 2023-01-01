from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    birthdate = models.DateField()