# Generated by Django 4.0.6 on 2022-07-24 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_orderitem_quantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
    ]