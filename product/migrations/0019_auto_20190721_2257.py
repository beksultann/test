# Generated by Django 2.2.2 on 2019-07-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20190721_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vat',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
    ]
