from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView, ListView

from posts.forms import PostForm
from posts.models import Post
from user.models import ProfileUser


def creating_post(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'create_posts.html', {'form': form})
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.created_by = user
            forms.save()
            return redirect('posts')
        return render(request, 'create_posts.html', {'form': form})


# def posts(request):


# post = Post.objects.all()
# profile = ProfileUser.objects.get()
# return render(request, 'index.html', {'posts': post, 'profile': profile})


class PostsView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'
