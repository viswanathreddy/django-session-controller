from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User
from django.conf import settings
from .models import SessionStore
from importlib import import_module


class SessionController(MiddlewareMixin):
    """
    Control no of sessions of the user
    """
    def process_request(self, request):
        if (request.is_authenticated):
            cur_session = SessionStore.objects.create(user=request.user, session_key=request.session.session_key)
            session_control_app_level = getattr(settings, "SESSION_CONTROL_APP_LEVEL", None)
            max_session_cnt = getattr(settings, "MAX_SESSION_CNT", None)
            if session_control_app_level and max_session_cnt:
                cur_session_cnt = SessionStore.objects.filter(user=request.user, is_active=True).count()
                if cur_session_cnt > max_session_cnt:
                    engine = import_module(settings.SESSION_ENGINE)
                    engine.SessionStore(cur_session.session_key).delete()
