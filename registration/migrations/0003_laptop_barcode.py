# Generated by Django 5.0.6 on 2024-05-10 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_remove_guest_staff_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='barcode',
            field=models.ImageField(blank=True, upload_to='laptop_barcodes/'),
        ),
    ]
