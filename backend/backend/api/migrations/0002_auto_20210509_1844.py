# Generated by Django 3.1.7 on 2021-05-09 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movie',
            new_name='Event',
        ),
    ]
