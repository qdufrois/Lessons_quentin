# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dashboard.models import Status, Subscription, Lesson


admin.site.register(Status)
admin.site.register(Subscription)
admin.site.register(Lesson)
