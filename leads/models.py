# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_delete
from django.utils.translation import ugettext_lazy as _


class Register(models.Model):
    """
    Register model to gather information among the visitors of the lead page
    """
    email = models.EmailField(unique=True)
    name = models.CharField(_('Name'), max_length=50, blank=True)
    created_on = models.DateTimeField(_('Created on'), auto_now_add=True)
    modified_on = models.DateTimeField(_('Modified on'), auto_now=True)

    class Meta:
        verbose_name = _('Register')
        verbose_name_plural = _('Registers')

    def __str__(self):
        return self.email


def delete_files_handler(sender, instance, **kwargs):
    for field in instance._meta.fields:
        if isinstance(field, models.FileField):
            f = getattr(instance, field.name)
            if f:
                f.delete(save=False)


class Newsletter(models.Model):
    """
    Defines a newsletter to send to regsistered users
    """

    from_name = models.CharField(_('From name'), max_length=50)
    from_address = models.EmailField(_('From address'))
    subject = models.CharField(_('Subject'), max_length=255)
    html_file = models.FileField(_('HTML file'), upload_to='newsletters')
    created_on = models.DateTimeField(_('Created on'), auto_now_add=True)
    modified_on = models.DateTimeField(_('Modified on'), auto_now=True)

    def __str__(self):
        return self.subject


post_delete.connect(delete_files_handler, Newsletter)
