# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from account.models import Account, Student


class TestAccountViews(TestCase):
    def setUp(self):
        self.client = Client()
        # Creation and login of a new user for the authentification
        self.user = User.objects.create_user(
            id="1",
            username="test1",
            first_name="test",
            last_name="test",
            email="test@test.com",
            password="Test123456",
        )
        self.client.login(username="test1", password="Test123456")
        # Creation of a test account
        Account.objects.create(
            account_id=1,
            name="Test_account",
            email="testget@gmail.com",
            password="Maman246",
            address="25 rue de la Corniche",
        )
        # Those data sets are going to be used for further test POST
        self.data_account = {
            "name": "Test_Post",
            "email": "testpost@gmail.com",
            "password": "Maman246",
            "address": "25 rue de la Corniche",
        }
        self.data_student = {
            "account_id": 1,
            "first_name": "Test2",
            "last_name": "Student",
            "birthdate": "1970-01-01",
            "email": "teststudent@gmail.com",
        }

    def test_account_POST(self):
        """Testing if an account is well created from JSON data"""
        response_1 = self.client.post(
            reverse("account:post_account"),
            data=self.data_account,
            json=json.dumps(self.data_account),
        )
        # Checking the expected status and if the account has been created in the db
        self.assertEquals(response_1.status_code, 201)
        self.assertEquals(
            Account.objects.get(name="Test_Post").email, "testpost@gmail.com"
        )
        # Checking that if an account with the same name and password
        # already exists, a 400 error is generated
        response_2 = self.client.post(
            reverse("account:post_account"),
            data=self.data_account,
            json=json.dumps(self.data_account),
        )
        self.assertEquals(response_2.status_code, 400)
        content = response_2.json()
        # Testing the error message
        self.assertEquals(
            content["non_field_errors"],
            ["An account with these name and password already exists!"],
        )

    def test_account_GET(self):
        """Testing if the db data of an account are well displayed and recoverable via a get"""
        response = self.client.get(
            reverse("account:get_account"), kwargs={"account_id": 1}
        )
        # Checking the status code and the information displayed
        self.assertEquals(response.status_code, 200)
        content = response.json()
        self.assertEquals(content[0]["name"], "Test_account")
        # Checking the password is not displayed
        with self.assertRaises(KeyError):
            pwd = content[0]["password"]

    def test_student_POST(self):
        """Testing if a student is well created from JSON data"""
        response = self.client.post(
            reverse("account:post_student"),
            data=self.data_student,
            json=json.dumps(self.data_student),
        )
        # Checking the expected status and if the account has been created in the db
        self.assertEquals(response.status_code, 201)
        self.assertEquals(
            Student.objects.get(student_id=2).first_name, "Test2"
        )  # id = 2 because another student is created in account.tests

    def test_user_not_authenticated(self):
        """ Testing the authentification. If a user is not connected,
        he/she should receive a 403 status code.
        """
        # Testing for a get
        self.client.logout()
        response_get = self.client.get(
            reverse("account:get_account"), kwargs={"account_id": 1}
        )
        self.assertEquals(response_get.status_code, 403)
        # Testing for a post
        response_post = self.client.post(
            reverse("account:post_account"),
            data=self.data_account,
            json=json.dumps(self.data_account),
        )
        self.assertEquals(response_post.status_code, 403)

    def test_delete_student(self):
        """ Testing the deletion of a student"""
        response = self.client.delete(
            reverse("account:delete_student", kwargs={"pk": 1})
        )
        with self.assertRaises(ObjectDoesNotExist):
            student = Student.objects.get(pk=1)
