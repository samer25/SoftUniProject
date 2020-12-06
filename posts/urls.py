from django.urls import path

from posts.views import PostsView, CreatePost, PostEdit, PostDelete

urlpatterns = [
    path('create/<int:pk>', CreatePost.as_view(), name='create post'),
    path('allposts/', PostsView.as_view(), name='posts'),
    path('edit/<int:pk>', PostEdit.as_view(), name='post edit'),
    path('delete/<int:pk>', PostDelete.as_view(), name='post delete')

]
