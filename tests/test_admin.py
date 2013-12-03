#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-leads
------------

Tests for `django-leads` admin module.
"""

import os
from django.core.files import File
from django.test import TestCase
from django.test.client import RequestFactory
from leads.models import Register, Newsletter
from leads.admin import RegisterAdmin, NewsletterAdmin


class InitialDataMixin(object):
    """
    Setup initial data for testing
    """
    def setUp(self):
        self.factory = RequestFactory()
        self.register_admin = RegisterAdmin(Register, None)
        Register.objects.create(name='john', email='john@domain.com')
        Register.objects.create(name='alice', email='alice@domain.com')
        Register.objects.create(name='bob', email='bob@domain.com')


class TestRegisterAdmin(InitialDataMixin, TestCase):

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


class TestNewsletterAdmin(InitialDataMixin, TestCase):

    def setUp(self):
        super(TestNewsletterAdmin, self).setUp()
        with open(os.path.join(os.path.dirname(__file__), 'fixtures/newsletter.html')) as f:
            self.obj = Newsletter.objects.create(subject='Test newsletter',
                                                 from_name='John',
                                                 from_address='john@domain.com',
                                                 html_file=File(f))
        self.newsletter_admin = NewsletterAdmin(Newsletter, None)

    def test_send(self):
        request = self.factory.get('/')
        queryset = Newsletter.objects.all()
        response = self.newsletter_admin.send(request, queryset)
        self.assertEqual(response, 3)
