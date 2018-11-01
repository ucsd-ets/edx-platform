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
    

def edx_course_enrollment_deactivated(current_event, caliper_event):
    """
    Caliper specific log for edX course unenrollment
    """
    caliper_object = {
        'course_id': current_event['context']['course_id'],
        'user_id': caliper_event['user_id'],
        'mode': current_event['event']['mode']
    }
    caliper_event.update({
        'object': caliper_object,
        'type': 'Enrollment',
        'action': 'Deactivated'
    })
    caliper_event['actor']['type'] = 'Person'
    return caliper_event
