# Generated by Django 4.2.3 on 2024-11-25 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0014_packagebundle_bundle_banner'),
        ('USER', '0015_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketItems',
            fields=[
                ('baskteItem_id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='basket',
            name='basket_laptop_unit',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='basket_package_unit',
        ),
        migrations.AddField(
            model_name='basket',
            name='basket_total_price',
            field=models.BigIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='basketitems',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BASKET_MAIN', to='USER.basket'),
        ),
        migrations.AddField(
            model_name='basketitems',
            name='basket_laptop',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='LAPTOP_ITEMS', to='PRODUCT.laptop'),
        ),
        migrations.AddField(
            model_name='basketitems',
            name='basket_package',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='PACKAGE_ITEMS', to='PRODUCT.packagebundle'),
        ),
        migrations.AddField(
            model_name='basket',
            name='basket_items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ITEMS', to='USER.basketitems'),
        ),
    ]