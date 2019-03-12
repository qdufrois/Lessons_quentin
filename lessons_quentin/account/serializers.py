# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from account.models import Account, Student


class StudentSerializer(serializers.ModelSerializer):
    """ Serializing the informations of a student, and managing as unique 
    together the fields account_id, first_name and last_name
    """
    class Meta:
        model = Student
        fields = ("account_id", "first_name", "last_name", "email", "birthdate")
        validators = [
            UniqueTogetherValidator(
                queryset=Student.objects.all(),
                fields=("account_id", "first_name", "last_name"),
                message="This student already exist",
            )
        ]
        extra_kwargs = {"account_id": {"write_only": True}}


class AccountSerializer(serializers.ModelSerializer):
    """Serializing the informations of an account, and managing as unique
    together the fields name and password"""

    # To get nested students infos into the account display
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ("name", "email", "address", "password", "students")
        validators = [
            UniqueTogetherValidator(
                queryset=Account.objects.all(),
                fields=("name", "password"),
                message="An account with these name and password already exists!",
            )
        ]
        extra_kwargs = {"password": {"write_only": True}}
