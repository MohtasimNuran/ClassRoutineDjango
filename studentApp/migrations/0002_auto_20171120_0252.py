# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='std_Id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
