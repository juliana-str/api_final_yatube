# Generated by Django 3.2.16 on 2023-04-11 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20230411_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='following',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='following',
            new_name='author',
        ),
    ]
