# Generated by Django 2.2.2 on 2019-07-18 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_product_counter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='status',
        ),
    ]
