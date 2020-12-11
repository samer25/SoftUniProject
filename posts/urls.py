from django.urls import path

from posts.views import PostsView, CreatePost, PostEdit, PostDelete, like_post, dislike_post, PostDetails

urlpatterns = [
    path('create/<int:pk>', CreatePost.as_view(), name='create post'),
    path('allposts/', PostsView.as_view(), name='posts'),
    path('edit/<int:pk>', PostEdit.as_view(), name='post edit'),
    path('delete/<int:pk>', PostDelete.as_view(), name='post delete'),
    path('post_details/<int:pk>', PostDetails.as_view(), name='post detail'),
    path('like/<int:pk>', like_post, name='like post'),
    path('dislike/<int:pk>', dislike_post, name='dislike post'),

]
