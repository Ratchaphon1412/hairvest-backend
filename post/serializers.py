from rest_framework import serializers
from .models import Post, ImagePost, SavePost
from users.models import User
from users.serializers import UserSerializer


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePost
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    post_image = PostImageSerializer(many=True)
    userID = UserSerializer()

    class Meta:
        model = Post
        fields = '__all__'

    # def create(self, validated_data):
    #     post_image = validated_data.pop('post_image')

    #     userCreatetor = User.objects.get(
    #         id=validated_data['userID_id'])

    #     post = Post.objects.create(
    #         title=validated_data['title'], detials=validated_data['detials'], userID=userCreatetor)
    #     for image in post_image:
    #         ImagePost.objects.create(postID=post, **image)
    #     return post


class SavePostSerializer(serializers.ModelSerializer):
    postID = PostSerializer()
    userID = UserSerializer()

    class Meta:
        model = SavePost
        fields = '__all__'
