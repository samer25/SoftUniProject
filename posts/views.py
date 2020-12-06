from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from posts.forms import PostForm
from posts.models import Post
from user.models import ProfileUser


class CreatePost(CreateView):
    """User Creating posts view"""

    # get method viewing forms for creating posts
    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, 'create_posts.html', {'form': form})

    # post method verified forms fields if they valid if they are save it
    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.created_by = user
            forms.save()
            return redirect('posts')
        return render(request, 'create_posts.html', {'form': form})


# def creating_post(request, pk):
#     user = User.objects.get(pk=pk)
#     if request.method == 'GET':
#         form = PostForm()
#         return render(request, 'create_posts.html', {'form': form})
#     else:
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             forms = form.save(commit=False)
#             forms.created_by = user
#             forms.save()
#             return redirect('posts')
#         return render(request, 'create_posts.html', {'form': form})


# def posts(request):


# post = Post.objects.all()
# profile = ProfileUser.objects.get()
# return render(request, 'index.html', {'posts': post, 'profile': profile})


class PostsView(ListView):
    """viewing all posts from users"""
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'
    ordering = ['-date']


class PostEdit(UpdateView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.get(pk=kwargs['pk'])
        form = PostForm(instance=posts)
        return render(request, 'common/edit.html', {'form': form})


class PostDelete(DeleteView):
    def get(self, request, *args, **kwargs):
        return render(request, 'post_delete.html')

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        post.delete()
        return redirect('posts')

