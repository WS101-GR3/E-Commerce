# Generated by Django 4.2.3 on 2024-11-15 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0003_rename_product_issoldout_product_issoldout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_type',
            new_name='product_category',
        ),
    ]
