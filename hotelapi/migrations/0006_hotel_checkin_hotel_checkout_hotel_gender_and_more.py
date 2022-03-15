# Generated by Django 4.0.3 on 2022-03-12 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapi', '0005_rename_hotelapi_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='checkin',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='hotel',
            name='checkout',
            field=models.DateField(default=datetime.date(2022, 3, 13)),
        ),
        migrations.AddField(
            model_name='hotel',
            name='gender',
            field=models.CharField(default='M', max_length=6),
        ),
        migrations.AddField(
            model_name='hotel',
            name='guest_name',
            field=models.CharField(default='John Doe', max_length=60),
        ),
    ]