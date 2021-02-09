# Generated by Django 3.1.4 on 2021-01-21 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion_Forum', '0021_auto_20210121_0425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcategory',
            name='main',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, verbose_name='Транслит'),
        ),
        migrations.AddField(
            model_name='podcategory',
            name='father',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Discussion_Forum.category'),
        ),
    ]