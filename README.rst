=============================
django-leads
=============================

.. image:: https://badge.fury.io/py/django-leads.png
    :target: http://badge.fury.io/py/django-leads
    
.. image:: https://travis-ci.org/dnmellen/django-leads.png?branch=master
        :target: https://travis-ci.org/dnmellen/django-leads

.. image:: https://pypip.in/d/django-leads/badge.png
        :target: https://crate.io/packages/django-leads?version=latest


An easy, functional and customizable lead page for your next big thing, ready to use in your django project.

Documentation
-------------

The full documentation is at http://django-leads.rtfd.org.

Quickstart
----------

Install django-leads
++++++++++++++++++++++

.. code-block :: bash

    pip install django-leads  # Also auto installs all needed dependencies! :)

Settings
++++++++++++++++++++++

.. code-block :: python

    INSTALLED_APPS = (
        ...
        'floppyforms',
        'crispy_forms',
        'leads',
    )
    ...
    CRISPY_TEMPLATE_PACK = 'bootstrap3'

urls.py
++++++++++++++++++++++

.. code-block :: python

    ...
    import leads.urls

    urlpatterns = patterns('',
        ...
        url(r'^admin/', include(admin.site.urls)),
        url(r'^', include(leads.urls, namespace='leads')),
    )


Features
--------

* Basic lead page to act as a placeholder for your django project