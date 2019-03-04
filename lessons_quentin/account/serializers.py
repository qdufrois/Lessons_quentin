# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from account.models import Account, Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email', 'birthdate', 'account')
        validators = [
            UniqueTogetherValidator(
                queryset=Student.objects.all(),
                fields=("account", "first_name", "last_name"),
                message='This student already exist'
            )
        ]
    

class AccountSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('name', 'email', 'address', 'password', 'students')
        validators = [
            UniqueTogetherValidator(
                queryset=Account.objects.all(),
                fields=('name', 'password'),
                message='An account with these name and password already exists!'
            )
        ]

        def create(self, validated_data):
            students_data = validated_data.pop('students')
            account = Account.objects.create(**validated_data)
            for student_data in students_data:
                Account.objects.create(account=account, **student_data)
            return account
