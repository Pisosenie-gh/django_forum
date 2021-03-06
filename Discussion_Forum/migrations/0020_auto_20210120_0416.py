# Generated by Django 3.1.4 on 2021-01-20 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion_Forum', '0019_remove_forum_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=5000, verbose_name='Навание категории')),
                ('description', models.TextField(blank=True, default=None, verbose_name='Описание категории')),
            ],
        ),
        migrations.CreateModel(
            name='PodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=5000, verbose_name='Навание подкатегории')),
                ('description', models.TextField(blank=True, default=None, verbose_name='Описание категории')),
                ('father', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Discussion_Forum.category')),
            ],
        ),
        migrations.AlterField(
            model_name='forum',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Discussion_Forum.podcategory'),
        ),
    ]
