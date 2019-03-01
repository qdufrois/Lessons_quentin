# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import Account, Student


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    subscription_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)


class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    description = models.TextField(null=False)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    subscription_id = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True)
    



    

