# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-01 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
