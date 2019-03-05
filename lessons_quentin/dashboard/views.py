# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dashboard.models import Subscription, Status
from dashboard.serializers import SubStatusSerializer, SubSerializer


class UpdateStatusSubView(APIView):

    def get(self, request, format=None):
        subs = Subscription.objects.all()
        serializer = SubStatusSerializer(subs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:          
            subscription = Subscription.objects.get(subscription_id=request.data['subscription_id'])
            serializer = SubStatusSerializer(data=request.data)            
                              
            if serializer.is_valid():                           
                subscription.status = Status.objects.get(pk=serializer.data['status'])
                subscription.save()
                return Response('Status modified', status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist:       
            return Response('This subscription does not exist', status=status.HTTP_400_BAD_REQUEST)

#{"subscription_id":1, "status":1}