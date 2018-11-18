from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)

class UserSessionStore(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, related_name='session_stores', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    session_key = models.CharField(max_length=40, unique=True, db_index=True)
    ip_addr = models.CharField(max_length=120, blank=True, null=True)
    max_sessions = models.IntegerField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} : is_active : {}".format(self.user.username,self.is_active)
