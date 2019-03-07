# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from dashboard.models import Subscription, Lesson, Status
from account.models import Student
from account.serializers import StudentSerializer


class SubSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subscription
        fields = ('account_id',)


class SubStatusSerializer(serializers.ModelSerializer):

    # subscription_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Subscription.objects.all())

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
        

class EnrolStudent(serializers.ModelSerializer):

    lesson_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Lesson.objects.all())
    student_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Student.objects.all())

    class Meta:
        model = Lesson
        fields = ('lesson_id', 'student_id')   

    def save(self):
        lesson = self.validated_data['lesson_id']
        new_student = self.validated_data['student_id']
        lesson.student_id.add(new_student)                           
        lesson.save()

class LessonStudentSerializer(serializers.ModelSerializer):

    student_id = StudentSerializer(many=True)
    lesson_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Lesson.objects.all())
    
    class Meta:
        model = Lesson
        fields = ('lesson_id', 'date', 'description', 'student_id')  
    
    

