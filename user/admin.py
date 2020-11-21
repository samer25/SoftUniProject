from django.contrib import admin

# Register your models here.
from user.models import ProfileUser

admin.site.register(ProfileUser)
