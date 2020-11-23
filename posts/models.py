from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class Post(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    img_post = models.ImageField(upload_to='image_posts')
    date = models.DateField(default=timezone.now)

