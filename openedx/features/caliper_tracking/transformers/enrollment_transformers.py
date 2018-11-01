"""
Transformers for all course related events.
"""


def edx_course_enrollment_activated(current_event, caliper_event):
    """
    When a student enrolls in a course, the server emits an edx.course.enrollment.activated event.

    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """
    caliper_event.update({
        'ip': current_event['ip'],
        'object': current_event['event'],
        'status': current_event['event']['mode'],
        'page': current_event['page'],
        'type': 'Membership',
        'action': 'Activated',
        'course_id': current_event['event']['course_id']
    })
    caliper_event['actor']['type'] = 'Person'
    return caliper_event
