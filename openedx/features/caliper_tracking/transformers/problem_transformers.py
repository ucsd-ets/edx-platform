"""
Transformers for all the problems events
"""

import json


def problem_show(current_event, caliper_event):
    """
    The browser emits problem_show events when the answer to a
    problem is shown; that is, the user selected Show Answer.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """
    current_event_details = json.loads(current_event['event'])

    caliper_object = {
        'id': current_event['referer'],
        'extensions': {
            'problem': current_event_details['problem']
        },
        'type': 'DigitalResource'
    }

    caliper_event.update({
        'action': 'Viewed',
        'type': 'ViewEvent',
        'object': caliper_object
    })

    caliper_event['referrer'].update({
        'type': 'WebPage'
    })

    caliper_event['actor'].update({
        'name': current_event['username'],
        'type': 'Person'
    })

    caliper_event['extensions']['extra_fields'].update({
        'course_id': current_event['context']['course_id'],
        'event': current_event['event'],
        'ip': current_event['ip']
    })

    return caliper_event


def problem_save(current_event, caliper_event):
    """
    The browser emits problem_save events when the answer to a
    problem is save instead of submitting; that is,
    the user selected Save Answer.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """
    caliper_object = {
        'id': current_event['referer'],
        'extensions': {
            'event': current_event['event']
        },
        'type': 'Assessment'
    }
    caliper_event.update({
        'action': 'Paused',
        'type': 'AssessmentEvent',
        'object': caliper_object
    })
    caliper_event['referrer'].update({
        'type': 'WebPage'
    })
    caliper_event['actor'].update({
        'name': current_event['username'],
        'type': 'Person'
    })
    caliper_event['extensions']['extra_fields'].update({
        'course_id': current_event['context']['course_id'],
        'ip': current_event['ip']
    })
    return caliper_event
