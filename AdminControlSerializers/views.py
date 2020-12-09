from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
# import viewsets
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import viewsets

# import local data
from posts.models import Post, CommentPostModel
from user.models import ProfileUser
from .serializers import UserSerializer, ProfileSerializer, PostSerializer, CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = User.objects.all()
    # specify serializer to be used
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = ProfileUser.objects.all()
    # specify serializer to be used
    serializer_class = ProfileSerializer


class PostViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Post.objects.all()

    # specify serializer to be used
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = CommentPostModel.objects.all()

    # specify serializer to be used
    serializer_class = CommentSerializer
