from django.shortcuts import render

# Create your views here.
from user.models import ProfileUser


def landing_page(request):
    return render(request, 'landing_page.html')

