# Generated by Django 3.1.7 on 2022-03-02 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_item_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='customer',
        ),
    ]
