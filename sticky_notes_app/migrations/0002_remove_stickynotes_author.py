# Generated by Django 5.0.6 on 2024-06-08 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sticky_notes_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stickynotes',
            name='author',
        ),
    ]
