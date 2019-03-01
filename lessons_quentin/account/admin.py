# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from account.models import Account, Student

admin.site.register(Account)
admin.site.register(Student)
