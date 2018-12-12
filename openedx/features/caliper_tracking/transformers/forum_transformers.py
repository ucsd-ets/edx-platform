"""
Transformers for all the forums events
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


def edx_forum_thread_created(current_event, caliper_event):
    """
    Users create a new top-level thread, also known as a post, by clicking
    New Post and then submitting their contributions. When these actions
    are complete, the server emits an edx.forum.thread.created

    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """

    current_event_details = current_event['event']

    caliper_object = {
        'body': current_event_details.pop('body', ''),
        'id': current_event['referer'],
        'type': 'Message',
        'name': current_event_details.pop('title', ''),
        'extensions': current_event_details
    }

    caliper_event.update({
        'type': 'MessageEvent',
        'action': 'Posted',
        'object': caliper_object
    })

    caliper_event['extensions']['extra_fields'].update({
        'ip': current_event['ip'],
        'course_id': current_event['context']['course_id'],
        'course_user_tags': current_event['context']['course_user_tags']
    })

    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })

    caliper_event['referrer']['type'] = 'WebPage'

    return caliper_event
