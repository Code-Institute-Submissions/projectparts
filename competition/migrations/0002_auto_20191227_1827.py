# Generated by Django 3.0 on 2019-12-27 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20191227_1827'),
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.Entries'),
        ),
    ]
