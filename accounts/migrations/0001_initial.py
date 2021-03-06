# Generated by Django 2.2.5 on 2019-11-08 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default='Phone No.', max_length=11)),
                ('address_line_1', models.CharField(default='Address Line 1', max_length=40)),
                ('address_line_2', models.CharField(blank=True, default='Address Line 2', max_length=40)),
                ('town_city', models.CharField(default='Town / City', max_length=40)),
                ('county', models.CharField(default='County', max_length=40)),
                ('country', models.CharField(default='Country', max_length=40)),
                ('postcode', models.CharField(default='Postcode', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
