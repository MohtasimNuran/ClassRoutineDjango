# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_Id', models.AutoField(primary_key=True, serialize=False)),
                ('exam_code', models.CharField(max_length=500)),
                ('exam_year', models.CharField(max_length=500)),
                ('exam_student_year', models.CharField(max_length=500)),
                ('exam_student_semester', models.CharField(max_length=500)),
            ],
        ),
    ]
