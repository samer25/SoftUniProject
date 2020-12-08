# Generated by Django 3.1.3 on 2020-12-08 09:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0016_auto_20201207_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentpostmodel',
            name='user_comm',
            field=models.ManyToManyField(related_name='user_comm', to=settings.AUTH_USER_MODEL),
        ),
    ]
