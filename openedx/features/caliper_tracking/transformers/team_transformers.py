"""
Transformers for all the teams related events
"""

import json


def edx_team_page_viewed(current_event, caliper_event):
    """
    When a user views any page with a unique URL under the Teams page in the
    courseware, the browser emits an edx.team.page_viewed event.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """

    current_event_details = json.loads(current_event['event'])

    caliper_object = {
        'id': current_event['page'],
        'type': 'WebPage',
        'extensions': current_event_details
    }

    caliper_event.update({
        'type': 'ViewEvent',
        'action': 'Viewed',
        'object': caliper_object
    })

    caliper_event['extensions']['extra_fields'].update({
        'ip': current_event['ip'],
        'course_id': current_event['context']['course_id'],
    })

    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })

    caliper_event['referrer']['type'] = 'WebPage'

    return caliper_event
