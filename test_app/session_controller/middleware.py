from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User
from django.conf import settings
from .models import UserSessionStore
from importlib import import_module
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages

class SessionController(MiddlewareMixin):
    """
    Control no of sessions of the user
    """
    def process_request(self, request):
        # import pdb;pdb.set_trace()
        if request.user.is_authenticated():
            cur_session, created = UserSessionStore.objects.get_or_create(user=request.user, session_key=request.session.session_key)
            print("session created ", created, request.user)
            session_config = getattr(settings, "SESSION_CONTROL_CONFIG")
            session_control_app_level = session_config.get("SESSION_CONTROL_APP_LEVEL", None)
            max_session_cnt = session_config.get("MAX_SESSION_CNT", None)
            if session_control_app_level and max_session_cnt:
                cur_session_cnt = UserSessionStore.objects.filter(user=request.user, is_active=True).count()
                session_control_user_level = session_config.get("SESSION_CONTROL_USER_LEVEL", None)
                if cur_session_cnt > max_session_cnt or (cur_session_cnt > cur_session.max_sessions if session_control_user_level else False):
                    engine = import_module(settings.SESSION_ENGINE)
                    cur_session.is_active = False
                    cur_session.save()
                    print("deleting session ", cur_session)
                    engine.SessionStore(cur_session.session_key).delete()
                    # print("after session deletion", request.session.session_key)
                    # request.session.modified = True
                    print("before http redirect")
                    messages.error(request, 'multiple sessions are not allowed to this view')
                    return HttpResponseRedirect(settings.LOGIN_URL, messages)
