from django.urls import path

from posts.views import PostsView, CreatePost

urlpatterns = [
    path('create/<int:pk>', CreatePost.as_view(), name='create post'),
    path('allposts/', PostsView.as_view(), name='posts'),

]
