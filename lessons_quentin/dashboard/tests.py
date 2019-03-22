# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from account.models import Account, Student
from dashboard.models import Subscription, Status, Lesson


class TestDashboardViews(TestCase):
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
        self.client.force_login(self.user)
        # Creation of a test account, test status, test subscription,
        # test student and test lesson instances
        Account.objects.create(
            account_id=1,
            name="Test_account",
            email="testget@gmail.com",
            password="Maman246",
            address="25 rue de la Corniche",
        )
        Status.objects.create(status_id=1, name="ACTIVE")
        Subscription.objects.create(
            subscription_id=1,
            account=Account.objects.get(account_id=1),
            status=Status.objects.get(status_id=1),
        )
        Student.objects.create(
            student_id=1,
            account=Account.objects.get(account_id=1),
            first_name="Test",
            last_name="Student",
            birthdate="1970-01-01",
            email="teststudent@gmail.com",
        )
        Lesson.objects.create(
            lesson_id=1,
            subscription=Subscription.objects.get(subscription_id=1),
            description="First test lesson",
        )
        # Those data sets are going to be used for further test POST
        self.data_sub = {"account_id": 1}
        self.data_status = {"subscription_id": 1, "status": 1}
        self.data_lesson = {
            "subscription_id": 1,
            "date": "2019-03-05",
            "description": "This a test lesson",
        }
        self.data_enrol = {"lesson_id": 1, "student_id": 1}
        self.data_lock = {"locked": True}

    def test_sub_POST(self):
        """Testing if a subscriptions is well created from JSON data"""
        response = self.client.post(
            reverse("dashboard:post_sub"),
            data=self.data_sub,
            json=json.dumps(self.data_sub),
        )
        # Checking the expected response status and if the subscription
        # has been created in the db
        self.assertEquals(response.status_code, 201)
        self.assertEquals(
            Subscription.objects.get(subscription_id=2).account.name, "Test_account"
        )

    def test_sub_status_POST(self):
        """Testing if a subscriptions status is well updated from JSON data"""
        response = self.client.post(
            reverse("dashboard:update_status"),
            data=self.data_status,
            json=json.dumps(self.data_status),
        )
        # Checking the expected reponse status and if the subscription's status
        # has been updated in the db
        self.assertEquals(response.status_code, 201)
        self.assertEquals(
            Subscription.objects.get(subscription_id=1).status.name, "ACTIVE"
        )

    def test_lesson_POST(self):
        """Testing if a lesson is well created from JSON data"""
        response = self.client.post(
            reverse("dashboard:post_lesson"),
            data=self.data_lesson,
            json=json.dumps(self.data_lesson),
        )
        # Checking the expected response status and if the lesson
        # has been created in the db
        self.assertEquals(response.status_code, 201)
        self.assertEquals(
            Lesson.objects.get(lesson_id=2).description, "This a test lesson"
        )

    def test_sub_GET(self):
        """Testing if the db data of a subscription are well displayed and 
        recoverable via a get
        """
        response = self.client.get(reverse("dashboard:get_sub", kwargs={"pk": 1}))
        # Checking the status code and the information displayed,
        # includind nested informations on status and lessons
        self.assertEquals(response.status_code, 200)
        content = response.json()
        self.assertEquals(content["status"]["name"], "ACTIVE")
        self.assertEquals(content["lessons"][0]["description"], "First test lesson")

    def test_enrol_student_POST(self):
        """Testing if a relationship between a lesson and a student 
        is well created from JSON data"""
        response = self.client.post(
            reverse("dashboard:enrol_student"),
            data=self.data_enrol,
            json=json.dumps(self.data_enrol),
        )
        # Checking the expected reponse status and if the relationship
        # has been created in the db
        self.assertEquals(response.status_code, 201)
        lesson = Lesson.objects.get(pk=1)
        self.assertEquals(lesson.students.get(pk=1).first_name, "Test")

    def test_lesson_GET(self):
        """Testing if the db data of a lesson are well displayed and 
        recoverable via a get
        """
        # Adding a student to the lesson
        response = self.client.post(
            reverse("dashboard:enrol_student"),
            data=self.data_enrol,
            json=json.dumps(self.data_enrol),
        )
        response = self.client.get(reverse("dashboard:get_lesson", kwargs={"pk": 1}))
        # Checking the status code and the information displayed,
        # includind nested informations on the students
        self.assertEquals(response.status_code, 200)
        content = response.json()
        self.assertEquals(content["description"], "First test lesson")
        self.assertEquals(content["students"][0]["first_name"], "Test")

    def test_lock_lesson_PATCH(self):
        """Testing if a lesson is well locked via a patch request. 
        A locked lesson should refuse any new relationship with a student
        """
        data = json.dumps(self.data_lock)  # The format differs from post method
        # otherwise I get a 415 status code response
        response = self.client.patch(
            reverse("dashboard:lock_lesson", kwargs={"pk": 1}),
            data=data,
            content_type="application/json",
        )
        # Checking the expected reponse status and if the locked
        # field has been well updated to True
        self.assertEquals(response.status_code, 200)
        lesson = Lesson.objects.get(pk=1)
        self.assertTrue(lesson.locked)
        # Trying to create a relationship with a student
        # and confirming it is denied
        response = self.client.post(
            reverse("dashboard:enrol_student"),
            data=self.data_enrol,
            json=json.dumps(self.data_enrol),
        )
        self.assertEquals(response.status_code, 403)

    def test_account_sub_GET(self):
        """Testing if the db data of an account and its subscriptions
        are well displayed and recoverable via a get
        """
        response = self.client.get(reverse("dashboard:account_sub", kwargs={"pk": 1}))
        # Checking the status code and the information displayed,
        # includind nested informations on subscription and status
        self.assertEquals(response.status_code, 200)
        content = response.json()
        self.assertEquals(content["name"], "Test_account")
        self.assertEquals(content["subscriptions"][0]["status"]["name"], "ACTIVE")

    def test_status_GET(self):
        """Testing if the db data of a status are well displayed and recoverable via a get"""
        response = self.client.get(reverse("dashboard:all_status"))
        # Checking the status code and the information displayed
        self.assertEquals(response.status_code, 200)
        content = response.json()
        self.assertEquals(content[0]["name"], "ACTIVE")
