# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examApp', '0001_initial'),
        ('studentApp', '0009_remove_courseenrollment_courseenrollment_syllabus_id_fk'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseenrollment',
            name='courseEnrollment_exam_Id_Fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='examApp.Exam'),
            preserve_default=False,
        ),
    ]
