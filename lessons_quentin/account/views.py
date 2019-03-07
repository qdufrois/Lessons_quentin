# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
 
from account.models import Account, Student
from account.serializers import AccountSerializer


class ListAccountView(ListAPIView):
    """Overriding the ListAccountView to display either a list of all account or a specific 
    account depending on the url
    """    
    serializer_class = AccountSerializer

    def get_queryset(self):
        account_id = self.kwargs['account_id']
        if account_id:
            queryset = Account.objects.filter(account_id=account_id)
        else:
            queryset = Account.objects.all()
        return queryset

