# Generated by Django 4.2.3 on 2024-11-17 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0009_productbundle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productbundle',
            name='id',
        ),
        migrations.AddField(
            model_name='productbundle',
            name='unit_id',
            field=models.BigAutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
