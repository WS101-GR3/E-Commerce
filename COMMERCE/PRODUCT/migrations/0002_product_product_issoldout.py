# Generated by Django 4.2.3 on 2024-11-15 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_isSoldOut',
            field=models.BooleanField(default=False),
        ),
    ]
