from django.db import models
from users.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    detials = models.TextField()
    userID = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_user", blank=True)


class ImagePost(models.Model):
    image = models.TextField()
    postID = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_image", blank=True)


class SavePost(models.Model):
    postID = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="save_post", blank=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
