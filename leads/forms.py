# -*- coding: utf-8 -*-
from django.conf import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.translation import ugettext_lazy as _

import floppyforms as forms

from .models import Register


class RegisterForm(forms.ModelForm):
    """
    RegisterForm is intended to be a highly customizable ModelForm and
    the user can change the model associated to the form and form fields
    """

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', _('Submit')))
        super(RegisterForm, self).__init__(*args, **kwargs)

    class Meta:
        model = getattr(settings, 'LEADS_REGISTER_MODEL', Register)
        fields = getattr(settings, 'LEADS_REGISTER_FORM_FIELDS', ('name', 'email'))
