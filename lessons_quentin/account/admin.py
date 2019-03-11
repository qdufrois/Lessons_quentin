# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from account.models import Account, Student


class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "insert_date", "update_date")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "insert_date", "update_date")


admin.site.register(Account, AccountAdmin)
admin.site.register(Student, StudentAdmin)
