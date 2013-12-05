=============================
django-leads
=============================

.. image:: https://badge.fury.io/py/django-leads.png
    :target: http://badge.fury.io/py/django-leads
    
.. image:: https://travis-ci.org/dnmellen/django-leads.png?branch=master
        :target: https://travis-ci.org/dnmellen/django-leads

.. image:: https://coveralls.io/repos/dnmellen/django-leads/badge.png
        :target: https://coveralls.io/r/dnmellen/django-leads

.. image:: https://pypip.in/d/django-leads/badge.png
        :target: https://crate.io/packages/django-leads?version=latest


An easy, functional and customizable lead page for your next big thing, ready to use in your django project.

.. image:: https://raw.github.com/dnmellen/django-leads/master/assets/leads_pic_1.png

Documentation
-------------

The full documentation is at http://django-leads.rtfd.org.

Quickstart
----------

Install django-leads
++++++++++++++++++++++

.. code-block :: bash

    $ pip install django-leads  # Also auto installs all needed dependencies! :)

Or get the bleeding-edge version:

.. code-block :: bash

    $ pip install https://github.com/dnmellen/django-leads/archive/master.zip

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

Final touch
++++++++++++++++++++++

.. code-block :: bash

    $ python manage.py syncdb


Features
--------

* Works on Python 2.6, 2.7, 3.3
* Basic lead page to act as a placeholder for your django project
* Registers user's name and email into database
* Customizable and extendable models and forms
* Admin interface
* Export registered users to CSV
* Send newsletters to your users


.. image:: https://d2weczhvl823v0.cloudfront.net/dnmellen/django-leads/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

