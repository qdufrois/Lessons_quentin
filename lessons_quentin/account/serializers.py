# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from account.models import Account, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email', 'birthdate')
    

class AccountSerializer(serializers.ModelSerializer):

    students = StudentSerializer(many=True)

    class Meta:
        model = Account
        fields = ('name', 'email', 'address', 'students')

        def create(self, validated_data):
            students_data = validated_data.pop('students')
            account = Account.objects.create(**validated_data)
            for student_data in students_data:
                Account.objects.create(account=account, **student_data)
            return account
