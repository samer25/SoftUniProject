from django.contrib.auth.models import User
from rest_framework import serializers
from posts.models import Post, CommentPostModel
from user.models import ProfileUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ User Model Hyper linked Serializer """

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'profile', 'email', 'created_by')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    """ Profile Model Hyper linked Serializer """

    class Meta:
        model = ProfileUser
        fields = ('url', 'user', 'id', 'first_name', 'last_name', 'profile_pic', 'bio')
        read_only_fields = ['profile_pic']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """ Post Model Hyper linked Serializer """

    class Meta:
        model = Post
        fields = ('url', 'id', 'created_by', 'title', 'description', 'img_post', 'date', 'likes', 'post_in')
        read_only_fields = ['img_post']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """ Comments Model Hyper linked Serializer """

    class Meta:
        model = CommentPostModel
        fields = ('url', 'id', 'user_comm', 'post', 'comments', 'date')
