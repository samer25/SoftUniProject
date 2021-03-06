# Generated by Django 3.1.3 on 2020-12-07 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_delete_postcommentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentPostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('post', models.ManyToManyField(related_name='post_in', to='posts.Post')),
            ],
        ),
    ]
