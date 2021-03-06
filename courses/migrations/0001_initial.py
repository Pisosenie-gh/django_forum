# Generated by Django 3.1.4 on 2021-02-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4000, null=True, verbose_name='Название курса')),
                ('description', models.TextField(max_length=100000, null=True, verbose_name='Описание')),
                ('slug', models.CharField(blank=True, max_length=50000, null=True, verbose_name='Ссылка на платежку')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
