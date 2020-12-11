from django.shortcuts import render

# Create your views here.
from user.models import ProfileUser


# function view just for landing page
def landing_page(request):
    return render(request, 'common/landing_page.html')
