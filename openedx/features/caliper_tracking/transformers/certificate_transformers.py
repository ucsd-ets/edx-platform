"""
Transformers for all the certificate events
"""

from openedx.features.caliper_tracking.utils import get_certificate_url
from django.conf import settings


def edx_certificate_evidence_visited(current_event, caliper_event):
    """
    When a learner shares her certificates on social network sites such
    as LinkedIn, and the link back to the certificate is followed by some
    visitor to that social network site, the server emits an
    edx.certificate.evidence_visited event.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """

    user_id = current_event['event'].get('user_id')
    course_id = current_event['event'].get('course_id')

    certificate_uri = get_certificate_url(user_id, course_id)

    object_extensions = current_event['event']

    caliper_event.update({
        'type': 'Event',
        'action': 'Showed',
        'object': {
            'id': certificate_uri,
            'type': 'Document',
            'extensions': object_extensions
        }
    })

    caliper_event['actor'].update({
        'id': settings.LMS_ROOT_URL,
        'type': 'SoftwareApplication'
    })

    caliper_event['extensions']['extra_fields'].update({
        'ip': current_event.get('ip'),
        'referer': current_event.get('referer'),
        'username': current_event.get('username')
    })

    caliper_event['extensions']['extra_fields'].update(
        current_event['context']
    )

    caliper_event.pop('referrer')

    return caliper_event
