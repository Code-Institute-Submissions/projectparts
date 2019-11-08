# Generated by Django 2.2.5 on 2019-11-08 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('competition', '0001_initial'),
        ('checkout', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='competition_entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='competition.Competition'),
        ),
        migrations.AddField(
            model_name='entries',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.Product'),
        ),
        migrations.AddField(
            model_name='entries',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]