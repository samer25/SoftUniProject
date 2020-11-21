from django.urls import path
from user.views import register_user, home_page

urlpatterns = [
    path('register/', register_user, name='user register'),
    path('', home_page, name='home page'),
]
