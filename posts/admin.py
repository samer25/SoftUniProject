from django.contrib import admin

# Register your models here.
from posts.models import Post, CommentPostModel

"""Register models in admin and merge them in one using admin TabularInLine"""


# @admin.register(CommentPostModel)
class CommentAdmin(admin.TabularInline):
    model = CommentPostModel
    list_display = ("user_comm", "post_id", "comments", "date")
    search_fields = ("comments_startswith", "user_comm__startswith",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("created_by", "title", "description", "img_post", "date")
    search_fields = ("title__startswith", "description__startswith",)
    inlines = [
        CommentAdmin,
    ]

# admin.site.register(Post)
# admin.site.register(CommentPostModel)
