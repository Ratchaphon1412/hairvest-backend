from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from post.models import Post, ImagePost, SavePost
from users.models import User
from .serializers import PostSerializer, SavePostSerializer


# Create your views here.
class CreatePost(APIView):
    def put(self, request):

        user = User.objects.get(id=request.data['userID_id'])

        post = Post.objects.create(
            title=request.data['title'], detials=request.data['detials'], userID=user)
        post.save()

        for image in request.data['post_image']:
            ImagePost.objects.create(postID=post, **image)

        # serializer = PostSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data)
        return Response(PostSerializer(post).data)

    def get(self, request):

        allpost = Post.objects.all()
        print(type(allpost))
        print(allpost)

        return Response(PostSerializer(allpost, many=True).data)

    def post(self, request):

        user = User.objects.get(id=request.data['user_id'])

        # allMypost = Post.objects.filter(userID=user).values()
        allMypost = Post.objects.all().filter(userID=user)

        print(allMypost)

        if not allMypost:
            return Response({'allMypost': {}})
        else:
            return Response(PostSerializer(allMypost, many=True).data)


class SavePostView(APIView):
    def put(self, request):

        user = User.objects.get(id=request.data['userID_id'])
        post = Post.objects.get(id=request.data['postID_id'])

        savePost = SavePost.objects.create(
            userID=user, postID=post)
        savePost.save()

        return Response(SavePostSerializer(savePost).data)

    def get(self, request):

        user = User.objects.get(id=request.GET.get('user_id'))

        allSavePost = SavePost.objects.all().filter(userID=user)

        if not allSavePost:
            return Response({'allSavePost': {}})
        else:
            return Response(SavePostSerializer(allSavePost, many=True).data)

    def delete(self, request):

        user = User.objects.get(id=request.data['user_id'])
        post = Post.objects.get(id=request.data['post_id'])

        allSavePost = SavePost.objects.all().filter(
            userID=user, postID=post)

        if not allSavePost:

            return Response({'deletePost': 'not found'})
        else:
            allSavePost.delete()
            return Response({'deletePost': 'success'})
