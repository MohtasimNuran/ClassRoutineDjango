# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('othersApp', '0012_auto_20171128_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='holidayEnd_date',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='holidayStart_date',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
