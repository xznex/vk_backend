# Generated by Django 4.1.2 on 2022-11-13 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0005_remove_chatmember_is_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmember',
            old_name='member',
            new_name='members',
        ),
    ]
