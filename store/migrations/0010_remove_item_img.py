# Generated by Django 3.1.7 on 2022-02-27 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20220227_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='img',
        ),
    ]
