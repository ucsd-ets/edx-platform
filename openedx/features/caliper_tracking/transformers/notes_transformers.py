"""
Transformers for all the navigation events
"""

import json


def edx_course_student_notes_added(current_event, caliper_event):
    """
    The server emits an edx.course.student_notes.added event when the student's


    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """
    caliper_event.update(
        {
            'type': 'AnnotationEvent',
            'action': 'Tagged',
            'object': {
                'id': current_event['referer'],
                'type': 'DigitalResource',
                'extensions': json.loads(current_event['event'])
            }
        }
    )
    caliper_event['object']['extensions']['course_id'] = \
        current_event['context']['course_id']
    caliper_event['actor'].update({
        'name': current_event['username'],
        'type': 'Person'
    })
    caliper_event['referrer']['type'] = 'WebPage'
    caliper_event['extensions']['extra_fields'].update({
        'ip': current_event['ip'],
        'path': current_event['context']['path'],
    })
    return caliper_event
