# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApp', '0004_auto_20171203_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_code',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
