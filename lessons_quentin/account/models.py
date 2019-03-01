# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255) 
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    birthdate = models.DateField()
    email = models.EmailField()
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
