from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, FormView, CreateView, View, DeleteView
from posts.models import Post
from user.forms import RegisterUserForm, ProfileUserForm, LoginUserForm
from user.models import ProfileUser


class RegisterUser(CreateView):
    """
    Creating user and profile
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


# logging out the user
@login_required
def logout_user(request):
    logout(request)
    return redirect('landing page')


class ProfileView(DetailView):
    """Viewing Profile of the user and his posts"""

    @method_decorator(login_required(login_url='login user'))
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        posts = Post.objects.filter(created_by=kwargs['pk'])

        return render(request, 'profile.html',
                      {'posts': posts, 'pk': request.user.id, 'user_profile': user})


class EditProfile(UpdateView):
    """Editing the profile user"""

    # get method to view current profile data in the forms fields to change it
    @method_decorator(login_required(login_url='login user'))
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


class DeleteProfile(DeleteView):
    """Deleting user and all user content"""

    # get method tho view html page delete
    @method_decorator(login_required(login_url='login user'))
    def get(self, request, *args, **kwargs):
        return render(request, 'delete_profile.html')

    # post method to delete user
    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        user.delete()
        return redirect('landing page')
