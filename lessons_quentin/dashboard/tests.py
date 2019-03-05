# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.test import TestCase, Client
from django.urls import reverse

from account.models import Account
from dashboard.models import Subscription, Status


class TestDashboardViews(TestCase):

    def setUp(self):
        self.client = Client()
        Account.objects.create(name='Test_Get', email='testget@gmail.com', password='Maman246', address='25 rue de la Corniche')
        Status.objects.create(name='ACTIVE')
        self.data_sub = {"account": 1}
        self.data_status = {"subscription_id":1, "status":1}
    
    def test_sub_POST(self):
        response = self.client.post(reverse('dashboard:post_sub'), data=self.data_sub, json=json.dumps(self.data_sub))
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Subscription.objects.get(subscription_id=1).account.name, 'Test_Get')

    def test_sub_status_POST(self):
        response = self.client.post(reverse('dashboard:update_status'), data=self.data_status, json=json.dumps(self.data_status))
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Subscription.objects.get(subscription_id=1).status.name, 'ACTIVE')
