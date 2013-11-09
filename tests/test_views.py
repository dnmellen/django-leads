#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-leads
------------

Tests for `django-leads` views module.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from leads.models import Register


class TestIndexView(TestCase):

    def setUp(self):
        self.c = Client()

    def test_get_index(self):
        response = self.c.get(reverse('leads:index'))
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.c.post(reverse('leads:index'), {'name': 'john', 'email': 'john@domain.com'})
        self.assertRedirects(response, reverse('leads:thanks_register'))
        reg_user = Register.objects.get(name='john')
        self.assertEqual(reg_user.email, 'john@domain.com')
