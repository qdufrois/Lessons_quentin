# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from account.models import Account, Student


class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'name')


admin.site.register(Account, AccountAdmin)
admin.site.register(Student)
