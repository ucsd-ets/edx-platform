"""
Transformers for all the library content block events
"""
from django.conf import settings


def edx_librarycontentblock_content_removed(current_event, caliper_event):
    """
    The server emits an edx.librarycontentblock.content.removed event when a
    user revisits a randomized content block and one or more of the components
    that were previously delivered to that user can no longer be delivered.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """
    caliper_object = {
        'id': current_event['referer'],
        'type': 'AssessmentItem',
        'extensions': current_event['event']
    }

    caliper_event.update({
        'action': 'Deleted',
        'type': 'Event',
        'object': caliper_object
    })
    caliper_event['referrer'].update({
        'type': 'WebPage'
    })
    caliper_event['actor'].update({
        'id': settings.LMS_ROOT_URL,
        'type': 'SoftwareApplication'
    })

    caliper_event['extensions']['extra_fields'].update(current_event['context'])
    caliper_event['extensions']['extra_fields']['ip'] = current_event['ip']
    caliper_event['extensions']['extra_fields']['username'] = current_event['username']
    caliper_event['extensions']['extra_fields'].pop('session')

    return caliper_event
