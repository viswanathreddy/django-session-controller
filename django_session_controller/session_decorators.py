
from django.conf import settings
from .models import SessionStore

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)


def valid_store_session(function):
    def wrap(request, *args, **kwargs):
        cur_session = SessionStore.objects.create(user=request.user, session_key=request.session.session_key)
        session_control_app_level = getattr(settings, "SESSION_CONTROL_APP_LEVEL", False)
        max_session_cnt = getattr(settings, "MAX_SESSION_CNT", False)
        if session_control_app_level and max_session_cnt:
            cur_session_cnt = SessionStore.objects.filter(user=request.user, is_active=True).count()
            if cur_session_cnt > max_session_cnt:
                engine = import_module(settings.SESSION_ENGINE)
                engine.SessionStore(cur_session.session_key).delete()
    return wrap
