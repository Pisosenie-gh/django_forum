# Generated by Django 3.1.4 on 2021-02-16 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion_Forum', '0035_forumpopular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpopular',
            name='vopros',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Discussion_Forum.forum'),
        ),
    ]
