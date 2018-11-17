from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)

class SessionStore(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, null=False, related_name='user_session_store', on_delete=models.CASCADE)
    is_active = models.BooleanField(True)
    session_key = models.CharField(null=False, max_length=40, unique=True, db_index=True)
    ip_addr = models.CharField(null=False, max_length=45)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

