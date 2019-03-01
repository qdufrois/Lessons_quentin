from django.conf.urls import url
from django.contrib import admin
from rest_framework.generics import  CreateAPIView

from account import views
from account.models import Account
from account.serializers import AccountSerializer


app_name = 'account'

urlpatterns = [
    url(r'^(?:(?P<account_id>[0-9]+)/)?$', views.ListAccountView.as_view(), name='get_account'),
    url(r'^create', CreateAPIView.as_view(queryset=Account.objects.all(), serializer_class=AccountSerializer), name='post_account')
]
