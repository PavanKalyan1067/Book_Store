# Generated by Django 4.0.5 on 2022-08-21 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_confirm_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default='Address', max_length=300),
        ),
    ]
