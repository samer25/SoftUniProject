from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

# Create your views here.
from user.forms import RegisterUserForm, ProfileUserForm


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
            return redirect('home page')

        return render(request, 'register.html', {'form': user_form, 'profile_form': profile_form, })


def home_page(request):
    return render(request, 'index.html')
