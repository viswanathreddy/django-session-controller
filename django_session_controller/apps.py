from django.apps import AppConfig


class SessionControllerConfig(AppConfig):
    name = 'django_session_controller'

    def ready(self):
        import django_session_controller.session_signals
