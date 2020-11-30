from django.urls import path

from common.views import landing_page
from user.views import register_user, login_user, logout_user, ProfileView

urlpatterns = [
    path('register/', register_user, name='user register'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),

]
