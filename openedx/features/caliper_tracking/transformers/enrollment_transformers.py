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
