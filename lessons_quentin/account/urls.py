from django.conf.urls import url
from django.contrib import admin

from account import views


app_name = 'account'

urlpatterns = [
    url(r'^(?:(?P<account_id>[0-9]+)/)?$', views.ListAccountView.as_view()),
]
