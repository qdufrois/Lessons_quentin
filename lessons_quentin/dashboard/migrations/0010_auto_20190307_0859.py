# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-07 08:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("dashboard", "0009_auto_20190307_0834")]

    operations = [
        migrations.RenameField(
            model_name="subscription", old_name="account", new_name="account_id"
        )
    ]
