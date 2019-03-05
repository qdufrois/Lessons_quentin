# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.test import TestCase, Client
from django.urls import reverse

from account.models import Account
from dashboard.models import Subscription, Status, Lesson


class TestDashboardViews(TestCase):

    def setUp(self):
        self.client = Client()
        Account.objects.create(account_id=1, name='Test_Get', email='testget@gmail.com', password='Maman246', address='25 rue de la Corniche')
        Status.objects.create(status_id=1, name='ACTIVE')
        Subscription.objects.create(subscription_id=1, account_id=Account.objects.get(account_id=1))
        self.data_sub = {"account_id": 1}
        self.data_status = {"subscription_id":1, "status":1}
        self.data_lesson = {'subscription_id': 1,'date': '2019-03-05','description': 'This a test lesson'}
    
    def test_sub_POST(self):
        response = self.client.post(reverse('dashboard:post_sub'), data=self.data_sub, json=json.dumps(self.data_sub))
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Subscription.objects.get(subscription_id=2).account_id.name, 'Test_Get')

    def test_sub_status_POST(self):
        response = self.client.post(reverse('dashboard:update_status'), data=self.data_status, json=json.dumps(self.data_status))
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Subscription.objects.get(subscription_id=1).status.name, 'ACTIVE')        
    
    def test_lesson_POST(self):
        response = self.client.post(reverse('dashboard:post_lesson'), data=self.data_lesson, json=json.dumps(self.data_lesson))
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Lesson.objects.get(lesson_id=1).description, 'This a test lesson')
    
    # def test_sub_GET(self):
    #     # Find a way for the get function to accept the kwargs
    #     response = self.client.get(reverse('dashboard:get_sub'),  kwargs={'pk':1})
    #     self.assertEquals(response.status_code, 200)
    #     content = response.json()
    #     self.assertEquals(content[0]['status']['name'], 'ACTIVE')
    #     self.assertEquals(content[0]['lessons']['description'], 'This a test lesson')

