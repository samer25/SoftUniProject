from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, UpdateView, FormView, CreateView, View, DeleteView

from posts.models import Post, CommentPostModel
from user.forms import RegisterUserForm, ProfileUserForm, LoginUserForm
from user.models import ProfileUser

"""Functions views"""


class RegisterUser(CreateView):
    """
    Creating user with profile
    """

    # get method to view user and profile fields
    def get(self, request, *args, **kwargs):
        user_form = RegisterUserForm()
        profile_form = ProfileUserForm()
        return render(request, 'register.html', {'form': user_form, 'profile_form': profile_form, })

    # post method to verified fields if they are correctly if it is register the user
    def post(self, request, *args, **kwargs):
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


# @transaction.atomic
# def register_user(request):
#     if request.method == 'GET':
#         user_form = RegisterUserForm()
#         profile_form = ProfileUserForm()
#         return render(request, 'register.html', {'form': user_form, 'profile_form': profile_form, })
#     else:
#         user_form = RegisterUserForm(request.POST)
#         profile_form = ProfileUserForm(request.POST, request.FILES)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()
#             login(request, user)
#             return redirect('landing page')
#
#         return render(request, 'register.html', {'form': user_form, 'profile_form': profile_form, })


class LoginUser(FormView):
    """Log in the user"""

    # get method view login fields
    def get(self, request, *args, **kwargs):
        login_form = LoginUserForm()
        return render(request, 'login.html', {'form': login_form})

    # post method verified if the user it is exist if it log in
    def post(self, request, *args, **kwargs):
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


# def login_user(request):
#     if request.method == 'GET':
#         login_form = LoginUserForm()
#         return render(request, 'login.html', {'form': login_form})
#     else:
#         login_form = LoginUserForm(request.POST)
#         if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('landing page')
#             else:
#                 error = 'user or password is not valid!'
#                 return render(request, 'login.html', {'form': login_form, 'error': error})
#         return render(request, 'login.html', {'form': login_form})


# logging out the user
@login_required
def logout_user(request):
    logout(request)
    return redirect('landing page')


# def profile_user(request, pk):
#     post = Post.objects.filter(created_by=pk)
#     return render(request, 'profile.html', {'posts': post, 'pk': pk})

class ProfileView(DetailView):
    """Viewing Profile of the user and his posts"""

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        posts = Post.objects.filter(created_by=kwargs['pk'])

        return render(request, 'profile.html',
                      {'posts': posts, 'pk': user.profile.pk, 'user_profile': user})


class EditProfile(UpdateView):
    """Editing the profile user"""

    # get method to view current profile data in the forms fields to change it
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        profile = ProfileUser.objects.get(pk=user.profile.pk)
        form = ProfileUserForm(instance=profile)
        return render(request, 'common/edit.html', {'form': form})

    # post method to verified edited profile form field and save it
    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        profile = ProfileUser.objects.get(pk=user.profile.pk)
        form = ProfileUserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', kwargs['pk'])


# def edit_profile(request, pk):
#     user = User.objects.get(pk=pk)
#     profile = ProfileUser.objects.get(pk=user.profile.id)
#     if request.method == 'GET':
#         form = ProfileUserForm(instance=profile)
#         return render(request, 'edit.html', {'form': form})
#     else:
#         form = ProfileUserForm(request.POST, request.FILES, instance=profile)
#         form.save()
#         return redirect('profile', pk)


# def delete_profile(request, pk):
#     user = User.objects.get(pk=pk)
#     if request.method == 'GET':
#         return render(request, 'delete_profile.html')
#     else:
#         user.delete()
#         return redirect('landing page')


class DeleteProfile(DeleteView):
    """Deleting user and all user content"""

    # get method tho view html page delete
    def get(self, request, *args, **kwargs):
        return render(request, 'delete_profile.html')

    # post method to delete user
    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        user.delete()
        return redirect('landing page')
