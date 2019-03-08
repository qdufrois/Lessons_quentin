# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from account.models import Account, Student


class TestAccountViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(id='1', username='test1', first_name='test', last_name='test', email='test@test.com', password="Test123456")
        self.client.login(username='test1', password='Test123456')
        Account.objects.create(account_id=1, name='Test_Get', email='testget@gmail.com', password='Maman246', address='25 rue de la Corniche')
        self.data_account = {'name': 'Test_Post', 'email': 'testpost@gmail.com', 'password': 'Maman246', 'address': '25 rue de la Corniche'}
        self.data_student = {'account_id': 1, 'first_name': 'Test2', 'last_name': 'Student', 'birthdate': '1970-01-01', 'email': 'teststudent@gmail.com', }
        
    def test_account_POST(self):
        response_1 = self.client.post(reverse('account:post_account'), data=self.data_account, json=json.dumps(self.data_account))
        self.assertEquals(response_1.status_code, 201)
        self.assertEquals(Account.objects.get(name='Test_Post').email, 'testpost@gmail.com')
        # Checking that if an account with the same name and password already exists, a 400 error is generated
        response_2 = self.client.post(reverse('account:post_account'), data=self.data_account, json=json.dumps(self.data_account))
        self.assertEquals(response_2.status_code, 400)    
        content = response_2.json()
        self.assertEquals(content['non_field_errors'], ["An account with these name and password already exists!"])   
        
    def test_account_GET(self):
        response = self.client.get(reverse('account:get_account'),  kwargs={'account_id':1})
        self.assertEquals(response.status_code, 200)
        content = response.json()
        self.assertEquals(content[0]['name'], 'Test_Get')
        # Checking the password is not displayed
        with self.assertRaises(KeyError):
            pwd = content[0]['password']    

    def test_student_POST(self):
        response = self.client.post(reverse('account:post_student'), data=self.data_student, json=json.dumps(self.data_student))
        self.assertEquals(response.status_code, 201)    
        self.assertEquals(Student.objects.get(student_id=2).first_name, 'Test2') # id = 2 because another student is created in account.tests

    def test_user_not_authenticated(self):
        self.client.logout()
        response = self.client.post(reverse('account:post_account'), data=self.data_account, json=json.dumps(self.data_account))
        self.assertEquals(response.status_code, 403)


    