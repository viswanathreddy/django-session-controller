
from django.conf import settings
from .models import UserSessionStore
from importlib import import_module
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)


def unique_session(function):
    def wrap(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        if request.user.is_authenticated():
            cur_session, created = UserSessionStore.objects.get_or_create(user=request.user, session_key=request.session.session_key)
            print("view decorator ", created, cur_session)
            session_config = getattr(settings, "SESSION_CONTROL_CONFIG", False)
            if session_config and session_config.get("SESSION_CONTROL_VIEW_LEVEL", None):
                cur_session_cnt = UserSessionStore.objects.filter(user=request.user, is_active=True).count()
                if cur_session_cnt > 1:
                    print("deleting session in view", cur_session)
                    cur_session.is_active = False
                    cur_session.save()
                    engine = import_module(settings.SESSION_ENGINE)
                    engine.SessionStore(cur_session.session_key).delete()
                    messages.error(self.request, 'multiple sessions are not allowed to this view')
                    return HttpResponseRedirect(settings.LOGIN_URL, messages)
                    # raise Exception("Multiple sessions are not allowed to this view")
        return function(self, request, *args, **kwargs)
    return wrap
