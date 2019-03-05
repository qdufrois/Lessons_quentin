# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import Account, Student


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "name"
    
    def __str__(self):
        return self.name


class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    subscription_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='subscription')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, related_name='subscription', null=True)


class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    date = models.DateField(null=True)
    description = models.TextField()
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    subscription_id = models.ForeignKey(Subscription, on_delete=models.SET_NULL, related_name='lessons', null=True)
    student = models.ManyToManyField(Student)
    



    

