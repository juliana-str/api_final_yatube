# Generated by Django 3.2.16 on 2023-04-11 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_follow_check_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='following',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='following',
        ),
    ]
