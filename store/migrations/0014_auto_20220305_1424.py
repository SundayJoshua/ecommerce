# Generated by Django 3.1.7 on 2022-03-05 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_product_productid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='productId',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
