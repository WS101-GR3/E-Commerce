# Generated by Django 4.2.3 on 2024-11-24 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0005_laptop_banner_alter_packagebundle_bundle_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagebundle',
            name='CPU_cooler_unit',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bundle_CPU_COOLER', to='PRODUCT.product'),
        ),
        migrations.AddField(
            model_name='packagebundle',
            name='GPU_unit',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bundle_GPU', to='PRODUCT.product'),
        ),
        migrations.AddField(
            model_name='packagebundle',
            name='PSU_unit',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bundle_PSU', to='PRODUCT.product'),
        ),
        migrations.AddField(
            model_name='packagebundle',
            name='case_unit',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bundle_case', to='PRODUCT.product'),
        ),
    ]
