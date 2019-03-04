# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from dashboard.models import Subscription
from dashboard.serializers import SubStatusSerializer


class UpdateStatusSubView(CreateAPIView):

    queryset = Subscription.objects.all() 
    serializer_class = SubStatusSerializer
    
    def post(self, request, format=None):
        serializer = SubStatusSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            sub = Subscription.objects.get_or_create(id=serializer.data['id'], account=serializer.data['account'])
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

