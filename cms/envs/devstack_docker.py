""" Overrides for Docker-based devstack. """

from .devstack import *  # pylint: disable=wildcard-import, unused-wildcard-import

# Docker does not support the syslog socket at /dev/log. Rely on the console.
LOGGING['handlers']['local'] = LOGGING['handlers']['tracking'] = {
    'class': 'logging.NullHandler',
}

LOGGING['loggers']['tracking']['handlers'] = ['console']

LMS_BASE = 'localhost:18000'
CMS_BASE = 'localhost:18010'
LMS_ROOT_URL = 'http://{}'.format(LMS_BASE)

FEATURES.update({
    'ENABLE_COURSEWARE_INDEX': True,
    'ENABLE_LIBRARY_INDEX': True,
    'ENABLE_DISCUSSION_SERVICE': True,
})

CREDENTIALS_SERVICE_USERNAME = 'credentials_worker'

OAUTH_OIDC_ISSUER = '{}/oauth2'.format(LMS_ROOT_URL)

JWT_AUTH.update({
    'JWT_SECRET_KEY': 'lms-secret',
    'JWT_ISSUER': OAUTH_OIDC_ISSUER,
    'JWT_AUDIENCE': 'lms-key',
})

###############################################################################
# See if the developer has any local overrides.
if os.path.isfile(join(dirname(abspath(__file__)), 'private.py')):
    from .private import *  # pylint: disable=import-error,wildcard-import
