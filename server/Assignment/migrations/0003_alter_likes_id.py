# Generated by Django 4.1.3 on 2022-12-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assignment', '0002_remove_likes_dislikes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
