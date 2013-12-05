# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, TemplateView
from .utils import get_register_model, get_register_form_class


class IndexView(CreateView):
    """
    This view renders the main page
    """
    template_name = 'leads/index.html'
    model = get_register_model()
    form_class = get_register_form_class()

    def get_success_url(self):
        return reverse('leads:thanks_register')


class ThanksView(TemplateView):
    """
    Page that loads when someone registers successfully
    """
    template_name = "leads/thanks_register.html"
