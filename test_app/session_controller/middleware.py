from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User
from django.conf import settings
from .models import UserSessionStore
from importlib import import_module
from django.shortcuts import HttpResponseRedirect

class SessionController(MiddlewareMixin):
    """
    Control no of sessions of the user
    """
    def process_request(self, request):
        # import pdb;pdb.set_trace()
        if request.user.is_authenticated():
            cur_session, created = UserSessionStore.objects.get_or_create(user=request.user, session_key=request.session.session_key)
            print("session created ", created, request.user)
            session_control_app_level = getattr(settings, "SESSION_CONTROL_APP_LEVEL", None)
            max_session_cnt = getattr(settings, "MAX_SESSION_CNT", None)
            if session_control_app_level and max_session_cnt:
                cur_session_cnt = UserSessionStore.objects.filter(user=request.user, is_active=True).count()
                if cur_session_cnt > max_session_cnt:
                    engine = import_module(settings.SESSION_ENGINE)
                    cur_session.is_active = False
                    cur_session.save()
                    print("deleting session ", cur_session)
                    engine.SessionStore(cur_session.session_key).delete()
                    # print("after session deletion", request.session.session_key)
                    # request.session.modified = True
                    print("before http redirect")
                    return HttpResponseRedirect(settings.LOGIN_URL)
