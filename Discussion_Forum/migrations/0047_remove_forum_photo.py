# Generated by Django 3.1.4 on 2021-02-17 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion_Forum', '0046_auto_20210217_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='photo',
        ),
    ]