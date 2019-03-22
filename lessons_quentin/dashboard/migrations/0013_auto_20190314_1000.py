# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-14 10:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("dashboard", "0012_lesson_locked")]

    operations = [
        migrations.AlterModelOptions(name="lesson", options={"verbose_name": "Lesson"}),
        migrations.AlterModelOptions(name="status", options={"verbose_name": "Status"}),
        migrations.AlterModelOptions(
            name="subscription", options={"verbose_name": "Subscription"}
        ),
        migrations.RemoveField(model_name="subscription", name="account_id"),
    ]