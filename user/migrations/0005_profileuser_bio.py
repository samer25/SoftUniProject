# Generated by Django 3.1.3 on 2020-11-30 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201122_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]