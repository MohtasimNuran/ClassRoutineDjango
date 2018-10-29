# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('std_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('std_fullName', models.CharField(max_length=1000)),
                ('std_dept', models.CharField(choices=[('CSE', 'CSE'), ('IIT', 'IIT')], max_length=1000)),
                ('std_classRoll', models.CharField(max_length=500)),
                ('std_examRoll', models.CharField(max_length=1000)),
                ('std_registrationNumber', models.CharField(max_length=1000)),
                ('std_phone', models.CharField(max_length=255)),
                ('std_hall', models.CharField(choices=[('SRJ', 'SRJ'), ('MH', 'MH'), ('Vashani', 'Vashani'), ('Bangobondhu', 'Bangobondhu'), ('Khaleda Zia', 'Khaleda Zia')], max_length=500)),
                ('std_session', models.CharField(max_length=255)),
                ('std_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=500)),
            ],
        ),
    ]