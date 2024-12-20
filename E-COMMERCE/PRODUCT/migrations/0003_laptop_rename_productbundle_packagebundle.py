# Generated by Django 5.0.3 on 2024-11-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0002_alter_product_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('lap_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('graphic_card', models.CharField(max_length=100)),
                ('memory', models.CharField(max_length=100)),
                ('storage', models.CharField(max_length=100)),
                ('display', models.CharField(max_length=100)),
                ('camera', models.CharField(max_length=100)),
                ('battery', models.CharField(max_length=100)),
                ('power_supply', models.CharField(max_length=100)),
                ('keyboard', models.CharField(max_length=100)),
                ('wifi', models.BooleanField(default=False)),
                ('warranty', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='ProductBundle',
            new_name='PackageBundle',
        ),
    ]
