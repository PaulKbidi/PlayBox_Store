# Generated by Django 5.0 on 2024-05-13 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='promo',
            field=models.BooleanField(default=False),
        ),
    ]