# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from account.models import Account, Student


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('name', 'email', 'adress')