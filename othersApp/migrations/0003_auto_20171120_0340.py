# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('othersApp', '0002_holiday_holiday_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='holiday_date',
            field=models.CharField(max_length=255),
        ),
    ]
