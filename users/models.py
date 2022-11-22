from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None  # this is to remove the username field

    USERNAME_FIELD = 'email'  # this is the new username field
    REQUIRED_FIELDS = []  # remove the old username field


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name="user_profile", on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile', blank=True)
