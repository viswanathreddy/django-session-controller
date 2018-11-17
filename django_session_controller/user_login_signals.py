from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.conf import settings
from .models import SessionStore
from django.core.exceptions import ObjectDoesNotExist

@receiver(user_logged_in)
def _user_logged_in(sender, user, request, **kwargs):
    SessionStore.objects.create(user=user, session_key=request.session.session_key)

@receiver(user_logged_out)
def _user_logged_out(sender, user, request, **kwargs):
    try:
        session = SessionStore.objects.get(session_key=request.session.session_key)
        session.is_active = False
        session.save()
    except ObjectDoesNotExist:
        print("session object does not exist ", user)

