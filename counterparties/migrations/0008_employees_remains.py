# Generated by Django 2.2.2 on 2019-07-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counterparties', '0007_employees_prepayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='remains',
            field=models.IntegerField(default=0),
        ),
    ]
