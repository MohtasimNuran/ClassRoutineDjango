# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-13 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApp', '0006_priorityhandling'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_password',
            field=models.CharField(default=36, max_length=255),
        ),
    ]
