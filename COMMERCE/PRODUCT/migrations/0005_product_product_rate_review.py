# Generated by Django 4.2.3 on 2024-11-17 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0004_rename_product_type_product_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_rate',
            field=models.BigIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('review_context', models.TextField()),
                ('product_topic', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='PRODUCT.product')),
            ],
        ),
    ]
