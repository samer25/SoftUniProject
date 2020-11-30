from django.urls import path

from common.views import landing_page
from user.views import register_user, login_user, logout_user, ProfileView, edit_profile, delete_profile

urlpatterns = [
    path('register/', register_user, name='user register'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('edit-profile/<int:pk>', edit_profile, name='edit profile'),
    path('delete_profile/<int:pk>', delete_profile, name='delete profile'),

]
