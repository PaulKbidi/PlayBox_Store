# Generated by Django 5.0 on 2024-05-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(null=True, upload_to='products'),
        ),
    ]
