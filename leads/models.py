# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Register(models.Model):
    """
    Register model to gather information among the visitors of the lead page
    """
    email = models.EmailField()
    name = models.CharField(_('Name'), max_length=50, blank=True)

    class Meta:
        verbose_name = _('Register')
        verbose_name_plural = _('Registers')

    def __str__(self):
        return self.email
