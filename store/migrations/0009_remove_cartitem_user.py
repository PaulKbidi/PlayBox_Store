# Generated by Django 5.0 on 2024-05-17 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_cartitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='user',
        ),
    ]
