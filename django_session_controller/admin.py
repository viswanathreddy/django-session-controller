from django.contrib import admin
from .models import *


class SessionGroupAdmin(admin.ModelAdmin):
    """model admin for session group"""

    list_display = (
        'name',
        'created_at',
        'updated_at',
    )

    search_fields = ('name',)
    readonly_fields = ['created_at','updated_at']


class SessionSettingAdmin(admin.ModelAdmin):
    """model admin for session group"""
    session_group = models.OneToOneField(SessionGroup, related_name='session_setting', on_delete=models.CASCADE)
    no_of_sessions = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    list_display = (
        'session_group__name',
        'no_of_sessions',
        'created_at',
        'updated_at'
    )

    search_fields = ('session_group__name',)
    readonly_fields = ['created_at','updated_at']
