# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-11 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20190307_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='locked',
            field=models.BooleanField(default=False),
        ),
    ]