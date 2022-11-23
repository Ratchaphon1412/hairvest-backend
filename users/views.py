import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.core.files.storage import default_storage
from django.contrib.auth.hashers import make_password

from users.models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer

import jwt
import datetime


# Create your views here.


class RegisterView(APIView):
    def post(self, request):

        print(type(request.data))
        print(request.data)

        image = request.data.get('image')
        request.data.pop('image')

        if image is not None:
            # write file
            with default_storage.open('profile/'+image.name, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

        # serializer = UserSerializer(request.data, many=True)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        user = User.objects.create(name=request.data.get('name'), email=request.data.get(
            'email'), password=make_password(request.data.get('password')))
        user.save()

        userProfile = UserProfile.objects.create(
            user=user, profile_pic='profile/'+image.name)
        userProfile.save()

        serializer = UserProfileSerializer(userProfile)

        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret',
                           algorithm='HS256')

        response = Response()
        # response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):
    def post(self, request):
        # token = request.COOKIES.get('jwt')
        token = request.data.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            print("test")
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        image = UserProfile.objects.filter(user=user).first()
        serializer = UserProfileSerializer(image)

        return Response(serializer.data)


# class LogoutView(APIView):
#     def post(self, request):
#         response = Response()
#         # response.delete_cookie('jwt')
#         response.data = {
#             'message': 'success'
#         }
#         return response
