# Generated by Django 4.2.3 on 2024-11-18 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=250, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
