# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-07 08:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("dashboard", "0008_auto_20190305_1728")]

    operations = [
        migrations.RenameField(
            model_name="subscription", old_name="account_id", new_name="account"
        )
    ]
