# Generated by Django 4.1.1 on 2023-03-06 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0047_order_orderitem_order_shippingaddress_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='customer',
        ),
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
