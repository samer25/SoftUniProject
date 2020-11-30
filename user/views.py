from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.generic import DetailView

from posts.models import Post
from user.forms import RegisterUserForm, ProfileUserForm, LoginUserForm
from user.models import ProfileUser

"""Functions views"""


@transaction.atomic
def register_user(request):
    if request.method == 'GET':
        user_form = RegisterUserForm()
        profile_form = ProfileUserForm()
        return render(request, 'register.html', {'form': user_form, 'profile_form': profile_form, })
    else:
        user_form = RegisterUserForm(request.POST)
        profile_form = ProfileUserForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('landing page')

        return render(request, 'register.html', {'form': user_form, 'profile_form': profile_form, })


def login_user(request):
    if request.method == 'GET':
        login_form = LoginUserForm()
        return render(request, 'login.html', {'form': login_form})
    else:
        login_form = LoginUserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('landing page')
            else:
                error = 'user or password is not valid!'
                return render(request, 'login.html', {'form': login_form, 'error': error})
        return render(request, 'login.html', {'form': login_form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('landing page')


# def profile_user(request, pk):
#     post = Post.objects.filter(created_by=pk)
#     return render(request, 'profile.html', {'posts': post, 'pk': pk})

class ProfileView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        post = Post.objects.filter(created_by=self.kwargs['pk'])
        return {'posts': post, 'pk': self.kwargs['pk']}
