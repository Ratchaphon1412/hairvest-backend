from django.db import models
from users.models import User, UserProfile

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    detials = models.TextField()
    userProfileImage = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="post_user", blank=True)


class ImagePost(models.Model):
    image = models.ImageField(upload_to='post', blank=True)
    post = models.OneToOneField(
        Post, on_delete=models.CASCADE, related_name="post_image", blank=True)


class SavePost(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="save_post", blank=True)
    user = models