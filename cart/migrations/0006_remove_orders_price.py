# Generated by Django 2.2.5 on 2019-11-16 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_orders_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='price',
        ),
    ]
