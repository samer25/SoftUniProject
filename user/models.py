from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ProfileUser(models.Model):
    first_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10, blank=True)
    profile_pic = models.ImageField(upload_to='profile_img', blank=True)
    bio = models.TextField(blank=True,)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
