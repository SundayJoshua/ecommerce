# Generated by Django 4.1.1 on 2022-10-13 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0043_delete_shippingaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
