from django.db import models
from users.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    detials = models.TextField()
    userID = models.ForeignKey(User, on_delete=models.CASCADE)


class ImagePost(models.Model):
    image = models.ImageField(upload_to='images/')
    postID = models.ForeignKey(Post, on_delete=models.CASCADE)
