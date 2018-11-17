from django.apps import AppConfig


class SessionControllerConfig(AppConfig):
    name = 'session_controller'

    def ready(self):
        import session_controller.session_signals
