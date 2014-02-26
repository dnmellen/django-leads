# -*- coding: utf-8 -*-
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset, ButtonHolder
from django.utils.translation import ugettext_lazy as _

import floppyforms as forms
from .utils import get_register_model, get_register_form_fields


class RegisterForm(forms.ModelForm):
    """
    RegisterForm is intended to be a highly customizable ModelForm and
    the user can change the model associated to the form and form fields
    """

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('Register here!'),
                Field('name'),
                Field('email'),
                ButtonHolder(
                    Submit('submit', _('Submit'), css_class="btn btn-danger")
                ),
            ),
        )
        super(RegisterForm, self).__init__(*args, **kwargs)

    class Meta:
        model = get_register_model()
        fields = get_register_form_fields()
