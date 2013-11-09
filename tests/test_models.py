#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase

from leads.models import Register


class TestRegisterModel(TestCase):

    def setUp(self):
        self.obj = Register.objects.create(name='john', email='john@domain.com')

    def test_str(self):
        self.assertEqual(str(self.obj), 'john@domain.com')
