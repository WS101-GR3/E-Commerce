# Generated by Django 4.2.3 on 2024-11-24 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0014_packagebundle_bundle_banner'),
        ('USER', '0009_alter_basket_basket_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitems',
            name='basket_laptop',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='LAPTOP_ITEMS', to='PRODUCT.laptop'),
        ),
        migrations.AlterField(
            model_name='basketitems',
            name='basket_package',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='PACKAGE_ITEMS', to='PRODUCT.packagebundle'),
        ),
    ]