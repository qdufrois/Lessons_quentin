# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from dashboard.models import Subscription, Lesson, Status


class SubSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subscription
        fields = ('account_id',)


class SubStatusSerializer(serializers.ModelSerializer):

    subscription_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Subscription.objects.all())

    class Meta:

        model = Subscription
        fields = ('subscription_id', 'status',)


class LessonSerializer(serializers.ModelSerializer):   
    
    class Meta:

        model = Lesson
        fields = ('lesson_id', 'subscription_id', 'date', 'description')                   
        extra_kwargs = {'subscription_id': {'write_only': True}}


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('status_id', 'name')


class SubLessonSerializer(serializers.ModelSerializer):

        status = StatusSerializer()
        lessons = LessonSerializer(many=True)

        class Meta:
            model = Subscription
            fields = ('subscription_id', 'status', 'subscription_date','lessons', )
        

        
           