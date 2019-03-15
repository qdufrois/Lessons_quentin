# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Account"
        unique_together = ("name", "password")

    def __str__(self):
        return self.name


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True)
    email = models.EmailField(null=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    account = models.ForeignKey(
        Account, related_name="students", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Student"
        unique_together = ("account", "first_name", "last_name")

    def __str__(self):
        return self.first_name + " " + self.last_name
