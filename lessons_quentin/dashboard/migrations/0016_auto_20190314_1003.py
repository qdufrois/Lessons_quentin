# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-14 10:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("dashboard", "0015_auto_20190314_1003")]

    operations = [
        migrations.RenameField(
            model_name="lesson", old_name="student_id", new_name="students"
        )
    ]
