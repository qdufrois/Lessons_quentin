# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from dashboard.models import Subscription, Lesson, Status
from account.models import Student, Account
from account.serializers import StudentSerializer


class SubSerializer(serializers.ModelSerializer):
    """Serializer used to create a new subscription, linked to an account"""

    class Meta:

        model = Subscription
        fields = ("account_id",)


class LessonSerializer(serializers.ModelSerializer):
    """Serializing the informations of a lesson"""

    class Meta:

        model = Lesson
        fields = ("lesson_id", "subscription_id", "date", "description")
        extra_kwargs = {"subscription_id": {"write_only": True}}


class StatusSerializer(serializers.ModelSerializer):
    """Serializing the informations of a status"""

    class Meta:
        model = Status
        fields = ("status_id", "name")


class SubStatusSerializer(serializers.ModelSerializer):
    """Serializer used to add a status to a subcription"""

    class Meta:

        model = Subscription
        fields = ("subscription_id", "status")


class SubLessonSerializer(serializers.ModelSerializer):
    """Serializing the informations of a subscriptions, and allows
    for the displays of nested statuses and lessons informations
    """

    # To get a nested display
    status = StatusSerializer()
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Subscription
        fields = ("subscription_id", "status", "subscription_date", "lessons")


class EnrolStudent(serializers.ModelSerializer):
    """Serializer used to create a relationship between a lesson and a student"""

    lesson_id = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Lesson.objects.all()
    )
    student_id = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Student.objects.all()
    )

    class Meta:
        model = Lesson
        fields = ("lesson_id", "student_id")

    def save(self):
        """Overriden method to check if the lesson is not locked, and then
        only create a link between a student and a lesson
        """
        lesson = self.validated_data["lesson_id"]
        if lesson.locked:
            return True
        new_student = self.validated_data["student_id"]
        lesson.student_id.add(new_student)
        lesson.save()


class LessonStudentSerializer(serializers.ModelSerializer):
    """Serializing the informations of a lesson, and allows
    for the displays of nested student informations
    """

    # To get a nested display
    student_id = StudentSerializer(many=True)
    lesson_id = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Lesson.objects.all()
    )

    class Meta:
        model = Lesson
        fields = ("lesson_id", "date", "description", "student_id")


class LockedLessonSerializer(serializers.ModelSerializer):
    """Serializer used to lock/unlock a lesson"""

    class Meta:
        model = Lesson
        fields = ("locked",)


class SubStatusSerializerExtended(serializers.ModelSerializer):
    """Serializer used to display nested informations about a subscription
    in the following AccounSubSerializer
    """

    # To get a nested display
    status = StatusSerializer()

    class Meta:

        model = Subscription
        fields = ("subscription_id", "status")


class AccountSubSerializer(serializers.ModelSerializer):
    """Serializing the informations of an account, and allows
    for the displays of nested subscriptions informations
    """

    # To get a nested display
    subscriptions = SubStatusSerializerExtended(many=True)

    class Meta:
        model = Account
        fields = ("name", "email", "subscriptions")
