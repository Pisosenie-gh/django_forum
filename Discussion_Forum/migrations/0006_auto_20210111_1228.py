# Generated by Django 3.1.4 on 2021-01-11 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion_Forum', '0005_reviews_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='user_photo',
            field=models.FileField(blank=True, upload_to='comments/'),
        ),
    ]