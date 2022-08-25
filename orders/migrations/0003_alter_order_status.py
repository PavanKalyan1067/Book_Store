# Generated by Django 4.0.5 on 2022-08-19 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_cart_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('CART', 'Ca'), ('ORDER', 'Or'), ('WISHLIST', 'Wl')], default='CART', max_length=10),
        ),
    ]
