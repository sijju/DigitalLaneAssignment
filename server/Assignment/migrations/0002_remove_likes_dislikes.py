# Generated by Django 4.1.3 on 2022-12-29 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Assignment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='dislikes',
        ),
    ]
