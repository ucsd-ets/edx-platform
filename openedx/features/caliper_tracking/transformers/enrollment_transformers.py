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
    The server emits an enrollment.deactivated event when the student's
    enrollment is cancelled.

    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
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


def edx_course_enrollment_mode_changed(current_event, caliper_event):
    """
    The server emits an enrollment.mode_changed event when the student's
    enrollment mode is changed.

    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """
    caliper_event.update({
        'type': 'Enrollment',
        'action': 'Mode_Changed',
        'object': current_event['event'],
        'course_id': current_event['context']['course_id']
    })

    caliper_event['actor']['type'] = 'Person'
    return caliper_event


def edx_course_enrollment_upgrade_clicked(current_event, caliper_event):
    """
    The server emits an enrollment.upgrade_clicked event when the student
    clicks on Upgrade Enrollment Button.

    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """

    caliper_object = {
        'id': current_event['page'],
        'name': 'Open edX Enrollment Upgrade',
    }

    caliper_event.update({
        'type': 'NavigationEvent',
        'action': 'NavigatedTo',
        'course_id': current_event['context']['course_id'],
        'object': caliper_object
    })

    caliper_event['actor']['type'] = 'Person'

    return caliper_event
