# Generated by Django 3.1.4 on 2021-01-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion_Forum', '0025_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='user_photo',
            field=models.CharField(blank=True, max_length=50000, verbose_name='Photo'),
        ),
    ]
