# Generated by Django 3.1.7 on 2021-05-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210509_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='end',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='events',
            name='start',
            field=models.CharField(max_length=32),
        ),
    ]