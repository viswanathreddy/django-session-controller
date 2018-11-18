
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
How to use :
==================================
1. Add django-session-controller to your Django project's settings module:



    INSTALLED_APPS = [
        ...
        'django-session-controller',
        ...
    ]
    
    MIDDLEWARE = [
        ...
        'django-session-controller.middleware.SessionController',
        ...
    ]
2. Apply the carrot migrations to your project's database:

.. code-block:: python

    python manage.py migrate django-session-controller
    
3.Put the below code to your Django project's settings module inorder to configure:

.. code-block:: python
   
     #Restrict sessions
    SESSION_CONTROL_CONFIG = {
        'SESSION_CONTROL_APP_LEVEL': True, # to control no of sessions on App level
        'MAX_SESSION_CNT' : 2, # to control no of concurrent sessions 
        'SESSION_CONTROL_USER_LEVEL': True,# to control no of sessions for each user
        'SESSION_CONTROL_VIEW_LEVEL': True #control session at View level
    }
4.Use "@unique_session" decorator on view method to impose session restriction.
.. code-block:: python
    
    from django_session_controller.session_decorators import unique_session
    class IndexView(LoginRequiredMixin, ListView):
        @unique_session
        def get(self, request, *args, **kwargs):
            pass
5.To make you session monitoring system use the model 'UserSessionStore'.
.. code-block:: python

    from django_session_controller.models import UserSessionStore
    

