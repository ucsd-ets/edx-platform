from django.apps import AppConfig
from django.conf import settings


LOGIN_EVENT_EMITTER = 'openedx.features.ucsd_features.utils.emit_login_event'


class UcsdFeaturesConfig(AppConfig):
    name = 'openedx.features.ucsd_features'
    verbose_name = "UCSD Features"

    def ready(self):
        """
        To override the settings after third_party_auth.
        """
        if settings.FEATURES.get('ENABLE_THIRD_PARTY_AUTH') and hasattr(settings, 'SOCIAL_AUTH_PIPELINE'):
            settings.SOCIAL_AUTH_PIPELINE.append(LOGIN_EVENT_EMITTER)
