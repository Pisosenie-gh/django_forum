# Generated by Django 3.1.4 on 2021-01-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion_Forum', '0013_auto_20210115_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
