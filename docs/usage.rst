========
Usage
========

Start a django project from scratch
-----------------------------------

Create virtualenv
++++++++++++++++++++

.. code-block :: bash

    $ mkdir test_lead
    $ cd test_lead
    $ mkvirtualenv leads

Install from pip
++++++++++++++++++++

.. code-block :: bash

    $ pip install django-leads

Start a brand new django project
++++++++++++++++++++++++++++++++

.. code-block :: bash

    $ django-admin.py startproject mysite

Edit `settings.py`

.. code-block :: python

    INSTALLED_APPS = (
        ...
        'floppyforms',
        'crispy_forms',
        'leads',
    )
    ...
    CRISPY_TEMPLATE_PACK = 'bootstrap3'

Edit `urls.py`

.. code-block :: python

    ...
    import leads.urls

    urlpatterns = patterns('',
        ...
        url(r'^admin/', include(admin.site.urls)),
        url(r'^', include(leads.urls, namespace='leads')),
    )


Build database

.. code-block :: bash

    $ python manage.py syncdb

Launch server

.. code-block :: bash

    $ python manage.py runserver


Overriding templates
--------------------

To have a reference you can copy the current templates:

.. code-block :: bash

    $ cd <your_django_project_path>
    $ mkdir templates
    $ cd templates
    $ cp -r ~/.virtualenvs/<your_virtualenv>/lib/python2.7/site-packages/leads/templates/leads .

Make sure you can load templates from ``<your_django_project_path>/templates`` (check your ``settings.py``):

.. code-block :: bash

    PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
    TEMPLATE_DIRS = (
        os.path.join(PROJECT_PATH, '..', 'templates'),
    )

Now you can override any template contained in ``../templates/leads``


Advanced settings
-----------------

`django-leads` allows the user to set some settings to change the default behaviour

=============================== ======================================================
 Setting name                   Explanation
=============================== ======================================================
 ``LEADS_REGISTER_MODEL``       Define a custom Model to save data
 ``LEADS_REGISTER_MODEL_ADMIN`` Define a custom ModelAdmin class
 ``LEADS_REGISER_FORM_CLASS``   Define a custom FormModel to represent the form
 ``LEADS_REGISTER_FORM_FIELDS`` Specify the fields that will be shown in the form
=============================== ======================================================

