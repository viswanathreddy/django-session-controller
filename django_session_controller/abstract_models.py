from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)




class SessionGroup(models.Model):
    """docstring for SessionGroup."""
    name = models.CharField(max_length=40,unique=True,db_index=True)
    # user        = models.ForeignKey(User,related_name='session_groups',on_delete=models.SET_NULL,null=True,blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        """docstring for Meta."""
        abstract=True

    def __str__(self):
        return "group {}  have {} users".format(self.name,self.users.count())


class SessionSetting(models.Model):

    """For group setting"""
    session_group = models.OneToOneField(SessionGroup, related_name='session_setting', on_delete=models.CASCADE)
    no_of_sessions = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """docstring for Meta."""
        abstract=True

    def __str__(self):
        return "{} : access granted {}".format(self.user.username,self.no_of_access)
