# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from dashboard.models import Subscription


class SubSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subscription
        fields = ('account',)

class SubStatusSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subscription
        fields = ('account', 'status',)