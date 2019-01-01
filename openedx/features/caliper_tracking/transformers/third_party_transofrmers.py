"""
Transformers for all the Third-Party events
"""


def oppia_exploration_completed(current_event, caliper_event):
    """
    The server emits an oppia.exploration.completed event when
    a user completes an interaction with an Oppia exploration component.
    Oppia explorations do not emit grading events.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """
    caliper_object = {
        'id': current_event['referer'],
        'type': 'AssessmentItem',
        'extensions': current_event['event']
    }
    caliper_event['extensions']['extra_fields'].update({
        'ip': current_event['ip'],
        'course_id': current_event['context']['course_id'],
        'module': current_event['context']['module'],
        'course_user_tags': current_event['context']['course_user_tags'],
        'asides': current_event['context']['asides']
    })
    caliper_event.update({
        'type': 'Event',
        'action': 'Completed',
        'object': caliper_object
    })
    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })
    caliper_event['extensions']['extra_fields'].pop('session')
    caliper_event['referrer']['type'] = 'WebPage'
    return caliper_event
