# Generated by Django 3.0 on 2020-01-03 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200103_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fits',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.Vehicle'),
        ),
    ]