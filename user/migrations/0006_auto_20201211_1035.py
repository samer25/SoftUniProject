# Generated by Django 3.1.3 on 2020-12-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_profileuser_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='profile_pic',
            field=models.ImageField(default='default.png', upload_to='profile_img'),
        ),
    ]