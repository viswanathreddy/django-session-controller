
django-session-controller : A Configurable Session Controller
=============================

Controls number of Django Sessions can be created for a user.

Features:
==============================
- Can be configurable to restrict no of sessions on the whole application.
- Can be configurable to restrict no of sessions on a perticular view.
- Can be configurable to restrict no of sessions for each user.
- Can monitor present user sessions

How To Install:
===============================
To install django-session-controller, simply use pip :

``` {.sourceCode .bash}
$ pip install django-session-controller

```



Documentation
-------------

The full documentation is at https://django-restricted-sessions.readthedocs.org.

Quickstart
----------

Install django-restricted-sessions::

    pip install django-restricted-sessions

Then add it to your middleware after SessionMiddleware::

    MIDDLEWARE_CLASSES = [
        ....
        'django.contrib.sessions.middleware.SessionMiddleware',
        # 'django.contrib.auth.middleware.AuthenticationMiddleware',
        'restrictedsessions.middleware.RestrictedSessionsMiddleware',
        ....
    ]

When ``RESTRICTEDSESSIONS_AUTHED_ONLY`` setting enabled ensure this middleware is added after
``AuthenticationMiddleware`` such that the ``request.user`` is present.
