# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-05 09:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20190304_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='account',
            new_name='account_id',
        ),
    ]