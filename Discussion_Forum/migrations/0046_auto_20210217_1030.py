# Generated by Django 3.1.4 on 2021-02-17 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion_Forum', '0045_auto_20210216_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='images',
        ),
        migrations.AddField(
            model_name='forum',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d'),
        ),
    ]