from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from posts.models import Post, CommentPostModel
from user.models import ProfileUser
from .serializers import UserSerializer, ProfileSerializer, PostSerializer, CommentSerializer


class IsSuperUser(IsAdminUser):
    """creating permission for serializers only admin can access to use in class base view in permission classes"""

    def has_permission(self, request, view):
        return bool(request.user.is_superuser)


class UserViewSet(viewsets.ModelViewSet):
    """user view serializer """
    # define queryset
    queryset = User.objects.all()
    # specify serializer to be used
    serializer_class = UserSerializer
    # permission only for admin
    permission_classes = (IsSuperUser,)


class ProfileViewSet(viewsets.ModelViewSet):
    """Profile view serializer """

    # define queryset
    queryset = ProfileUser.objects.all()
    # specify serializer to be used
    serializer_class = ProfileSerializer
    # permission only for admin

    permission_classes = (IsSuperUser,)


class PostViewSet(viewsets.ModelViewSet):
    """Post view serializer """

    # define queryset
    queryset = Post.objects.all()

    # specify serializer to be used
    serializer_class = PostSerializer

    permission_classes = (IsSuperUser,)


class CommentViewSet(viewsets.ModelViewSet):
    """Comments view serializer """

    # define queryset
    queryset = CommentPostModel.objects.all()

    # specify serializer to be used
    serializer_class = CommentSerializer
    # permission only for admin

    permission_classes = (IsSuperUser,)
