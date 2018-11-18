
django-session-controller : A Configurable Session Controller
=============================

Django session controller controls the number of sessions a user can hold in application life cycle . Admin/Staff user can configure number of active user sessions at the app level or at the view level.

Features:
---------
- Can be configurable to restrict no of sessions on the whole application.
- Can be configurable to restrict no of sessions on a particular view.
- Can be configurable to restrict no of sessions for each user.
- Auditable user sessions history .

How To Install:
---------------
To install **django-session-controller** simply use pip :

``` {.sourceCode .bash}
$ pip install django-session-controller

```
How to use :
------------
1. Add **django-session-controller** to your Django project's settings module:


``` {.sourceCode .py}
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
```
2. Apply the **django-session-controller** migrations to your project's database:

``` {.sourceCode .py}

    python manage.py migrate django-session-controller

```
3.Put the below code to your Django project's settings module inorder to configure:

``` {.sourceCode .py}
   
     #Restrict sessions
    SESSION_CONTROL_CONFIG = {
        'SESSION_CONTROL_APP_LEVEL': True, # to control no of sessions on App level
        'MAX_SESSION_CNT' : 2, # to control no of concurrent sessions for any user
        'SESSION_CONTROL_USER_LEVEL': True,# to control no of sessions for each user
        'SESSION_CONTROL_VIEW_LEVEL': True #control session at View level
    }
```

4.Use **@unique_session** decorator on view method to impose session restriction.
``` {.sourceCode .py}
    
    from django_session_controller.session_decorators import unique_session
    class IndexView(LoginRequiredMixin, ListView):
        @unique_session
        def get(self, request, *args, **kwargs):
            pass
```
5.To make you session monitoring system use the model **UserSessionStore**.
``` {.sourceCode .py}

    from django_session_controller.models import UserSessionStore
```

Future Works :
--------------
- Support for token based Auth system
- Manage the session restriction on User group level
- A better session monitoring for admins

## Contributors
- [Naveen](https://github.com/naveen-varshney)
- [Sibasish](https://github.com/Sibasish1992)
- [Viswanath](https://github.com/viswanathreddy)

License
-------

The project is licensed under the MIT license.

