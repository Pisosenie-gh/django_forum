# Generated by Django 3.1.4 on 2021-02-16 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion_Forum', '0037_forum_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forum',
            old_name='image',
            new_name='images',
        ),
    ]