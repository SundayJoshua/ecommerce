# Generated by Django 3.1.7 on 2022-03-07 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
