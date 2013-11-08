# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

import floppyforms as forms

from .models import Register


class RegisterForm(forms.ModelForm):
    """
    RegisterForm is intended to be a highly customizable ModelForm and
    the user can change the model associated to the form and form fields
    """
    class Meta:
        model = getattr(settings, 'LEADS_REGISTER_MODEL', Register)
        fields = getattr(settings, 'LEADS_REGISTER_FORM_FIELDS', ('name', 'email'))
