# Generated by Django 5.0.6 on 2024-05-09 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='staff_id',
        ),
    ]
