"""
Transformers for all course related events.
"""


def edx_course_enrollment_activated(current_event, caliper_event):
    caliper_event.update({
        'ip': current_event['ip'],
        'object': current_event['event'],
        'status': current_event['event']['mode'],
        'page': current_event['page'],
        'type': 'Membership',
        'action': 'Activated'
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
