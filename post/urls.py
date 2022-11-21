from django.contrib import admin
from django.urls import path
from .views import CreatePost, SavePostView

urlpatterns = [
    path('post/', CreatePost.as_view()),
    path('post/save/', SavePostView.as_view())

]
