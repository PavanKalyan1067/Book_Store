# Generated by Django 4.0.5 on 2022-08-21 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
    ]
