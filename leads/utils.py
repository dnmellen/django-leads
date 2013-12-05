from importlib import import_module

from django.conf import settings


def get_class_from_string(import_string):

    try:
        from_list, import_name = import_string.rsplit('.', 1)
        return getattr(import_module(from_list), import_name)
    except (AttributeError, ValueError):  # pragma no cover
        raise ImportError(import_string)


def get_register_model():
    return get_class_from_string(getattr(settings, 'LEADS_REGISTER_MODEL', 'leads.models.Register'))


def get_register_model_admin():
    return get_class_from_string(getattr(settings, 'LEADS_REGISTER_MODEL_ADMIN', 'leads.admin.RegisterAdmin'))


def get_register_form_class():
    return get_class_from_string(getattr(settings, 'LEADS_REGISTER_FORM_CLASS', 'leads.forms.RegisterForm'))


def get_register_form_fields():
    return getattr(settings, 'LEADS_REGISTER_FORM_FIELDS', ('name', 'email'))
