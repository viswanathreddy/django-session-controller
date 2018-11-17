
from django.conf import settings
from .models import UserSessionStore
from importlib import import_module

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)


def valid_store_session(function):
    def wrap(request, *args, **kwargs):
        cur_session, created = UserSessionStore.objects.get_or_create(user=request.user, session_key=request.session.session_key)
        print("view decorator ", created, cur_session)
        max_session_cnt = getattr(settings, "MAX_SESSION_CNT", False)
        if max_session_cnt:
            cur_session_cnt = UserSessionStore.objects.filter(user=request.user, is_active=True).count()
            if cur_session_cnt > max_session_cnt:
                print("deleting session ", cur_session)
                cur_session.is_active = False
                cur_session.save()
                engine = import_module(settings.SESSION_ENGINE)
                engine.SessionStore(cur_session.session_key).delete()
    return wrap
