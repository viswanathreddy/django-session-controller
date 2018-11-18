from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User
from django.conf import settings
from .models import UserSessionStore
from importlib import import_module

from django_session_controller.models import UserSessionGroup

class SessionController(MiddlewareMixin):
    """
    Control no of sessions of the user
    """
    def process_request(self, request):
        if request.user and request.user.is_authenticated() and not request.user.is_staff:
            cur_session, created = UserSessionStore.objects.get_or_create(user=request.user, session_key=request.session.session_key)
            session_group = UserSessionGroup.objects.filter(user=request.user).first()
            if session_group:
                if hasattr(session_group,'session_setting'):
                    max_session_cnt = session_group.session_setting.no_of_sessions
                    cur_session_cnt = UserSessionStore.objects.filter(user=request.user, is_active=True).count()
                    if cur_session_cnt > max_session_cnt or (cur_session_cnt > cur_session.max_sessions if session_control_user_level else False):
                        engine = import_module(settings.SESSION_ENGINE)
                        cur_session.is_active = False
                        cur_session.save()
                        print("deleting session ", cur_session)
                        engine.SessionStore(cur_session.session_key).delete()
                        print("before http redirect")
                        messages.error(request, 'multiple sessions are not allowed to this view')
                        return HttpResponseRedirect(settings.LOGIN_URL, messages)
