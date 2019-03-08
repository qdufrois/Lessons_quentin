# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from account.models import Student
from dashboard.models import Subscription, Status, Lesson
from dashboard.serializers import SubStatusSerializer, SubSerializer, EnrolStudent


class UpdateStatusSubView(APIView):
    """This view allows to update the status field of a subscription, via a post request containing
    the subcription and the status instances ids.
    """
    def post(self, request, format=None):
        try:        
            subscription = Subscription.objects.get(subscription_id=request.data['subscription_id'])            
            serializer = SubStatusSerializer(subscription, data=request.data)
            if serializer.is_valid():   
                serializer.save()                        
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:       
            return Response('This subscription does not exist', status=status.HTTP_404_NOT_FOUND)   


class EnrolStudentView(APIView):
    """This view allows to create a relationship between a student and a lesson instances, via a post request
    containing their ids.
    """

    def post(self, request, format=None):               
        serializer = EnrolStudent(data=request.data) 
        if serializer.is_valid():
            serializer.save() # Method overrided to only create the relationship between the two instances
            return Response('Student added to lesson', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
