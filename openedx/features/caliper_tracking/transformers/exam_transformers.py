"""
Transformers for all timed and practice related exams.
"""


def edx_special_exam_timed_attempt_created(current_event, caliper_event):
    """
    The server emits this event when a learner chooses to take a special exam.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """
    assessment_name = current_event['event'].pop('exam_name')
    caliper_event.update({
        'type': 'Event',
        'action': 'Created',
        'object': {
            'id': current_event['referer'],
            'type': 'Attempt',
            'name': assessment_name,
            'extensions': current_event['event']
        }
    })
    caliper_event['extensions']['extra_fields'].update({
        'course_id': current_event['context']['course_id'],
    })
    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })
    caliper_event['referrer']['type'] = 'WebPage'
    caliper_event['extensions']['extra_fields']['ip'] = current_event['ip']
    return caliper_event
