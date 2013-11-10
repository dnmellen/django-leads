__version__ = '0.1.0'

from django.conf import settings


def get_register_model():
    from .models import Register
    return getattr(settings, 'LEADS_REGISTER_MODEL', Register)


def get_register_model_admin():
    from .admin import RegisterAdmin
    return getattr(settings, 'LEADS_REGISTER_MODEL_ADMIN', RegisterAdmin)


def get_register_form_class():
    from .forms import RegisterForm
    return getattr(settings, 'LEADS_REGISER_FORM_CLASS', RegisterForm)


def get_register_form_fields():
    return getattr(settings, 'LEADS_REGISTER_FORM_FIELDS', ('name', 'email'))
