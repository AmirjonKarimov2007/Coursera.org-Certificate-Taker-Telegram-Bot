# Generated by Django 5.0.1 on 2024-01-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100, verbose_name='Fullname')),
                ('username', models.CharField(max_length=100, null=True, verbose_name='Username')),
                ('telegram_id', models.BigIntegerField(default=1, unique=True, verbose_name='Telegram_id')),
            ],
        ),
    ]
