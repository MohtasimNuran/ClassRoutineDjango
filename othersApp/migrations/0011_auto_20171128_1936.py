# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('othersApp', '0010_holiday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='holidayStart_date',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='holiday_description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
