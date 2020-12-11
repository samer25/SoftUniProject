from django.contrib.auth.models import User

# Create your views here.
# import viewsets
from rest_framework import viewsets

# import local data
from rest_framework.permissions import IsAdminUser

from posts.models import Post, CommentPostModel
from user.models import ProfileUser
from .serializers import UserSerializer, ProfileSerializer, PostSerializer, CommentSerializer


class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser)


class UserViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = User.objects.all()
    # specify serializer to be used
    serializer_class = UserSerializer

    permission_classes = (IsSuperUser,)


class ProfileViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = ProfileUser.objects.all()
    # specify serializer to be used
    serializer_class = ProfileSerializer

    permission_classes = (IsSuperUser,)


class PostViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Post.objects.all()

    # specify serializer to be used
    serializer_class = PostSerializer

    permission_classes = (IsSuperUser,)


class CommentViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = CommentPostModel.objects.all()

    # specify serializer to be used
    serializer_class = CommentSerializer

    permission_classes = (IsSuperUser,)
