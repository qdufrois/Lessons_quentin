# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from account.models import Student
from dashboard.models import Subscription, Lesson
from dashboard.serializers import SubStatusSerializer, EnrolStudent


class UpdateStatusSubView(CreateAPIView):
    """This view allows to update the status field of a subscription, via a post 
    request containing the subcription and the status instances ids.
    """

    serializer_class = SubStatusSerializer
    queryset = Subscription.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            subscription = Subscription.objects.get(
                subscription_id=request.data["subscription_id"]
            )
            serializer = self.get_serializer(subscription, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(
                "This subscription does not exist", status=status.HTTP_404_NOT_FOUND
            )

class EnrolStudentView(CreateAPIView):
    """This view allows to create a relationship between a student and a lesson instances,
    via a post request containing their ids.
    """

    serializer_class = EnrolStudent

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Checking if the lesson is not locked, and overriding the .save method
            # to create the relationship between the two instances
            if not serializer.save():
                return Response(
                    "Student added to lesson", status=status.HTTP_201_CREATED
                )
            return Response(
                "Lesson full, no more student can be added",
                status=status.HTTP_403_FORBIDDEN,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

