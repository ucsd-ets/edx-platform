"""
Transformers for all the problems events
"""


def edx_forum_response_created(current_event, caliper_event):
    """
    Users create a reply to a post by clicking Add a Response and then submitting their contributions. When these
    actions are complete, the server emits an edx.forum.response.created event.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """

    caliper_object = {
        'id': current_event['referer'],
        'body': current_event['event'].pop('body'),
        'extensions': current_event['event'],
        'type': 'Message'
    }

    caliper_event.update({
        'action': 'Posted',
        'type': 'MessageEvent',
        'object': caliper_object
    })

    caliper_event['referrer']['type'] = 'WebPage'

    caliper_event['actor'].update({
        'name': current_event['username'],
        'type': 'Person'
    })

    caliper_event['extensions']['extra_fields'].update({
        'course_id': current_event['context']['course_id'],
        'ip': current_event['ip']
    })

    return caliper_event
