from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from post.models import Post, ImagePost, SavePost
from users.models import User, UserProfile
from .serializers import PostSerializer, SavePostSerializer, PostImageSerializer

from django.core.files.storage import default_storage


# Create your views here.
class CreatePost(APIView):
    def put(self, request):
        pass
        # user = User.objects.get(id=request.data['userID_id'])

        # post = Post.objects.create(
        #     title=request.data['title'], detials=request.data['detials'], userID=user)
        # post.save()

        # for image in request.data['post_image']:
        #     ImagePost.objects.create(postID=post, **image)

        # return Response(PostSerializer(post).data)

    def get(self, request):

        # allpost = Post.objects.all()
        # print(type(allpost))
        # print(allpost)

        allPostImage = ImagePost.objects.all()

        return Response(PostImageSerializer(allPostImage, many=True).data)

    def post(self, request):

        user = User.objects.get(id=request.data['userID'])

        userprofile = UserProfile.objects.get(user=user)

        post = Post.objects.create(
            title=request.data['title'], detials=request.data['detials'], userProfileImage=userprofile)
        post.save()

        imageUpload = request.data.get('post_image')

        if imageUpload is not None:
            with default_storage.open('post/'+imageUpload.name, 'wb+') as destination:
                for chunk in imageUpload.chunks():
                    destination.write(chunk)

        postImage = ImagePost.objects.create(
            post=post, image='post/'+imageUpload.name)

        return Response(PostImageSerializer(postImage).data)

        # user = User.objects.get(id=request.data['user_id'])

        # # allMypost = Post.objects.filter(userID=user).values()
        # allMypost = Post.objects.all().filter(userID=user)

        # print(allMypost)

        # if not allMypost:
        #     return Response({'allMypost': {}})
        # else:
        #     return Response(PostSerializer(allMypost, many=True).data)


class ViewPost(APIView):
    def get(self, request):
        postID = request.GET.get('id')

        post = Post.objects.get(id=postID)

        postImage = ImagePost.objects.all().filter(post=post)

        return Response(PostImageSerializer(postImage, many=True).data)

    def post(self, request):

        # userID = request.data['userID']

        userID = request.data.get('userID')

        userProfile = UserProfile.objects.get(user=userID)

        postImage = ImagePost.objects.all().filter(post__userProfileImage=userProfile)

        postSerializer = PostImageSerializer(postImage, many=True)

        return Response(postSerializer.data)


class SavePostView(APIView):
    def post(self, request):

        user = User.objects.get(id=request.data['userID'])

        print(request.data['userID'])
        print(request.data['postID'])
        userImage = UserProfile.objects.get(user=user)

        post = Post.objects.get(id=request.data['postID'])

        savePost = SavePost.objects.create(
            user=userImage, post=post)
        savePost.save()

        return Response(SavePostSerializer(savePost).data)

    def get(self, request):

        user = User.objects.get(id=request.GET.get('userID'))

        userImage = UserProfile.objects.get(user=user)

        allSavePost = SavePost.objects.all().filter(user=userImage)

        if not allSavePost:
            return Response({'allSavePost': {}})
        else:
            return Response(SavePostSerializer(allSavePost, many=True).data)

    def delete(self, request):

        user = User.objects.get(id=request.data['userID'])

        userImage = UserProfile.objects.get(user=user)
        post = Post.objects.get(id=request.data['postID'])

        allSavePost = SavePost.objects.all().filter(
            user=userImage, post=post)

        if not allSavePost:

            return Response({'deletePost': 'not found'})
        else:
            allSavePost.delete()
            return Response({'deletePost': 'success'})
