from django.contrib import admin

# Register your models here.
from user.models import ProfileUser


# admin.site.register(ProfileUser)


@admin.register(ProfileUser)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "id", "first_name", "last_name", "bio", "profile_pic")
    search_fields = ("title__user", "description__first_name",)
