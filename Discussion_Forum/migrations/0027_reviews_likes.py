# Generated by Django 3.1.4 on 2021-02-01 10:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Discussion_Forum', '0026_forum_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='likes',
            field=models.ManyToManyField(related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
