# Generated by Django 3.1.4 on 2021-01-11 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion_Forum', '0006_auto_20210111_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='user_photo',
            field=models.ImageField(blank=True, upload_to='comments/'),
        ),
    ]
