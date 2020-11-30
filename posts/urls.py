from django.urls import path

from posts.views import creating_post,  PostsView

urlpatterns = [
    path('create/<int:pk>', creating_post, name='create post'),
    path('allposts/', PostsView.as_view(), name='posts'),

]
