# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
 
from account.models import Account, Student
from account.serializers import AccountSerializer


class ListAccountView(ListAPIView):
    
    serializer_class = AccountSerializer

    def get_queryset(self):
        account_id = self.kwargs['account_id']
        if account_id:
            queryset = Account.objects.filter(account_id=account_id)
        else:
            queryset = Account.objects.all()
        return queryset