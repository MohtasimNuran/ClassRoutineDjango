# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 21:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0006_courseenrollment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseenrollment',
            name='courseEnrollment_exam_Id_Fk',
        ),
        migrations.RemoveField(
            model_name='courseenrollment',
            name='courseEnrollment_syllabus_Id_Fk',
        ),
    ]