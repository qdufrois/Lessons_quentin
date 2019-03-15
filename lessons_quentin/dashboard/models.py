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
        verbose_name = "Status"

    def __str__(self):
        return self.name


class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    subscription_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="subscriptions"
    )
    status = models.ForeignKey(
        Status, on_delete=models.SET_NULL, related_name="subscription", null=True
    )

    class Meta:
        verbose_name = "Subscription"

    def __str__(self):
        return "subscription n°" + str(self.subscription_id)


class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    date = models.DateField(null=True)
    description = models.TextField()
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    locked = models.BooleanField(default=False)

    subscription = models.ForeignKey(
        Subscription, on_delete=models.SET_NULL, related_name="lessons", null=True
    )
    students = models.ManyToManyField(Student)

    class Meta:
        verbose_name = "Lesson"

    def __str__(self):
        return "lesson n°" + str(self.lesson_id)
