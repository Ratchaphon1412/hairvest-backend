from rest_framework import serializers
from .models import Post, ImagePost


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'detials', 'userID']
