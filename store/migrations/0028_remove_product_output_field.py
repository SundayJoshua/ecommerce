# Generated by Django 3.1.7 on 2022-04-02 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_product_output_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='output_field',
        ),
    ]
