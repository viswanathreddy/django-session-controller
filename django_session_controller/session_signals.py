from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from importlib import import_module
from django.db.models.signals import pre_delete
from django.contrib.sessions.models import Session
from .models import UserSessionStore

@receiver(user_logged_in)
def _user_logged_in(sender, user, request, **kwargs):
    return

# @receiver(user_logged_out)
# def _user_logged_out(sender, user, request, **kwargs):
#     print("user logged out", user)
#     try:
#         session = SessionStore.objects.get(session_key=request.session.session_key)
#         session.is_active = False
#         session.save()
#     except ObjectDoesNotExist:
#         print("session object does not exist ", user)

@receiver(pre_delete, sender=Session, dispatch_uid='session_pre_delete')
def session_timeout(sender, instance, **kwargs):
    print("deleting session ", instance)
    UserSessionStore.objects.filter(session_key=instance.session_key).update(is_active=False)