# Generated by Django 5.0.3 on 2024-04-03 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='created',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='updated',
        ),
    ]