# Generated by Django 4.2.3 on 2024-11-24 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0013_packagebundle_bundle_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagebundle',
            name='bundle_banner',
            field=models.ImageField(default='Desert.jpg', upload_to=''),
        ),
    ]
