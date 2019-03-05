# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-05 10:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='account',
            new_name='account_id',
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together=set([('account_id', 'first_name', 'last_name')]),
        ),
    ]