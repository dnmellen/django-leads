#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from django.core.files import File
from django.test import TestCase

from leads.models import Register, Newsletter


class TestRegisterModel(TestCase):

    def setUp(self):
        self.obj = Register.objects.create(name='john', email='john@domain.com')

    def test_str(self):
        self.assertEqual(str(self.obj), 'john@domain.com')


class TestNewsletterModel(TestCase):

    def setUp(self):
        with open(os.path.join(os.path.dirname(__file__), 'fixtures/newsletter.html')) as f:
            self.obj = Newsletter.objects.create(subject='Test newsletter',
                                                 from_name='John',
                                                 from_address='john@domain.com',
                                                 html_file=File(f))

    def test_str(self):
        self.assertEqual(str(self.obj), 'Test newsletter')

    def test_delete(self):
        self.obj.delete()
        self.assertEqual(0, Newsletter.objects.all().count())
