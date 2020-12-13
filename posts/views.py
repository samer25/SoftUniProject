import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from posts.forms import PostForm, CommentPostForm
from posts.models import Post, CommentPostModel

"""CRUD FOR POSTS"""


class CreatePost(CreateView):
    """User Creating posts view that required to be login using method_decorator"""

    # get method viewing forms for creating posts
    @method_decorator(login_required(login_url='login user'))
    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, 'create_posts.html', {'form': form})

    # post method verified forms fields if they valid if they are save it
    @method_decorator(login_required(login_url='login user'))
    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.created_by = user
            forms.save()
            messages.success(request, 'Successfully Created Post')

            return redirect('posts')
        return render(request, 'create_posts.html', {'form': form})


# function view for like without render
@login_required(login_url='login user')
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    user = User.objects.get(pk=request.user.id)
    post.likes.add(user)
    post.save()

    return redirect('posts')


# function view for dislike without render
@login_required(login_url='login user')
def dislike_post(request, pk):
    post = Post.objects.get(pk=pk)
    user = User.objects.get(pk=request.user.id)
    post.likes.remove(user)
    post.save()
    return redirect('posts')


class PostsView(ListView):
    """ all posts from users and is it public"""
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'
    ordering = ['-date']


class PostDetails(DetailView):
    """Post details and Comments that require user login"""

    # get method view getting from selected user post details and adding form comment with comments that users comments
    @method_decorator(login_required(login_url='login user'))
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        user = User.objects.get(pk=post.created_by.pk)
        form = CommentPostForm()
        comments = CommentPostModel.objects.filter(post=kwargs['pk'])
        context = {'p': post, 'user_profile': user, 'form': form, 'comments': comments}
        return render(request, 'post_details.html', context)

    # post method verified forms comment fields if they valid
    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        user = User.objects.get(pk=post.created_by.pk)
        comments = CommentPostModel.objects.filter(post=kwargs['pk'])
        form = CommentPostForm(request.POST)
        context = {'posts': post, 'user_profile': user, 'form': form, 'comments': comments}
        if form.is_valid():
            comm = CommentPostModel(comments=form.cleaned_data['comments'], post_id=kwargs['pk'],
                                    user_comm_id=request.user.id)
            comm.post = post
            comm.save()
            messages.success(request, 'Successfully Commented The Post')

            return redirect('post detail', kwargs['pk'])
        return render(request, 'post_details.html',
                      context)


class PostEdit(UpdateView):
    """Post editing """

    # method get getting forms of selected post to edit it
    @method_decorator(login_required(login_url='login user'))
    def get(self, request, *args, **kwargs):
        posts = Post.objects.get(pk=kwargs['pk'])
        form = PostForm(instance=posts)
        return render(request, 'common/edit.html', {'form': form})

    # post method verified forms fields if they valid if they are update it
    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        path_img = post.img_post.path
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            os.remove(path_img)
            form.save()
            messages.success(request, 'Successfully Edited The Post')
            return redirect('posts')


class PostDelete(DeleteView):
    """Post Delete"""
    """Deleting the post with all connected models : comments model """

    @method_decorator(login_required(login_url='login user'))
    def get(self, request, *args, **kwargs):
        return render(request, 'post_delete.html')

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        os.remove(post.img_post.path)
        post.delete()
        messages.success(request, 'Successfully Deleted The Post')

        return redirect('posts')
