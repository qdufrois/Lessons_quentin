# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-05 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("dashboard", "0004_lesson_student")]

    operations = [
        migrations.AlterField(
            model_name="lesson", name="date", field=models.DateField(null=True)
        )
    ]
