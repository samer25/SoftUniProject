from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from posts.forms import PostForm
from posts.models import Post


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


def posts(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'posts': post})
