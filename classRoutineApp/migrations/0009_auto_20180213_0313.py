# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-12 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classRoutineApp', '0008_classroutine_semestertry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroutine',
            name='dayOfWeek',
            field=models.CharField(max_length=500),
        ),
    ]
