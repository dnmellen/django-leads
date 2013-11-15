#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-leads
------------

Tests for `django-leads` admin module.
"""

from django.test import TestCase
from django.test.client import RequestFactory
from leads.models import Register
from leads.admin import RegisterAdmin


class TestRegisterAdmin(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.register_admin = RegisterAdmin(Register, None)
        Register.objects.create(name='john', email='john@domain.com')
        Register.objects.create(name='alice', email='alice@domain.com')
        Register.objects.create(name='bob', email='bob@domain.com')

    def test_export_to_csv(self):
        expected_result = [['email', 'name'],
                           ['john@domain.com', 'john'],
                           ['alice@domain.com', 'alice'],
                           ['bob@domain.com', 'bob']]
        request = self.factory.get('/')
        queryset = Register.objects.all()
        response = self.register_admin.export_to_csv(request, queryset)
        self.assertEqual(response.status_code, 200)
        csv_response = [l.decode('utf-8').split(',')[:2] for l in response.content.splitlines()]
        self.assertEqual(expected_result, csv_response)
