# Generated by Django 3.0.2 on 2020-01-29 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200111_1744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]