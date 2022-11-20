from django.contrib import admin
from django.urls import path
from .views import CreatePost

urlpatterns = [
    path('post/', CreatePost.as_view()),

]
