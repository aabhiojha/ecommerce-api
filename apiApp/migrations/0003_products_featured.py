# Generated by Django 5.2.4 on 2025-07-05 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0002_alter_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]
