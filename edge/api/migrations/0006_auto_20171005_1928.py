# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_registrystudent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplineschedule',
            name='end_time',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='disciplineschedule',
            name='start_time',
            field=models.CharField(max_length=255),
        ),
    ]
