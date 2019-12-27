# Generated by Django 3.0 on 2019-12-27 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0001_initial'),
        ('cart', '0006_remove_orders_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='related_competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.Competition'),
        ),
    ]
