# Generated by Django 5.0.1 on 2024-01-15 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_data', '0006_certificate_created_at_certificate_updated_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
