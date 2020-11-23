from django.urls import path

from posts.views import creating_post, posts

urlpatterns = [
    path('create/<int:pk>', creating_post, name='create post'),
    path('allposts', posts, name='posts'),

]
