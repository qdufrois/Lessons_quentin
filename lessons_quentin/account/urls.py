from django.conf.urls import url
from django.contrib import admin
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from account import views
from account.models import Account, Student
from account.serializers import AccountSerializer, StudentSerializer


app_name = 'account'

urlpatterns = [    
    url(r'^(?:(?P<account_id>[0-9]+)/)?$', views.ListAccountView.as_view(), name='get_account'),
    url(r'^create$', CreateAPIView.as_view(queryset=Account.objects.all(), serializer_class=AccountSerializer), name='post_account'),
    url(r'^create_student$', CreateAPIView.as_view(queryset=Student.objects.all(), serializer_class=StudentSerializer), name='post_student'),
]
