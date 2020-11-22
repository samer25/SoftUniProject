from django.shortcuts import render

# Create your views here.
from posts.models import Post


def creating_post(request):
    pass


def posts(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'posts': post})
