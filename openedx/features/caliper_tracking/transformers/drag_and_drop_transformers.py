"""
Transformers for all the drag and drop events
"""


def edx_drag_and_drop_v2_item_dropped(current_event, caliper_event):
    """
    The server emits this event when a learner releases a draggable item
    into a target zone in a drag and drop problem.

    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """

    caliper_object = {
        'id': current_event['referer'],
        'extensions': current_event['event'],
        'type': 'AssessmentItem'
    }

    caliper_event.update({
        'action': 'Completed',
        'type': 'AssessmentItemEvent',
        'object': caliper_object
    })

    caliper_event['referrer'].update({
        'id': current_event['referer'],
        'type': 'WebPage'
    })

    caliper_event['actor'].update({
        'name': current_event['username'],
        'type': 'Person'
    })

    caliper_event['extensions']['extra_fields'].update(current_event['context'])
    caliper_event['extensions']['extra_fields']['ip'] = current_event['ip']
    caliper_event['extensions']['extra_fields'].pop('session')
    return caliper_event


def edx_drag_and_drop_v2_item_picked_up(current_event, caliper_event):
    """
    The server emits this event when a learner selects a draggable item in a
    drag and drop problem.

    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """

    caliper_object = {
        'id': current_event['referer'],
        'extensions': current_event['event'],
        'type': 'AssessmentItem'
    }

    caliper_event.update({
        'action': 'Started',
        'type': 'AssessmentItemEvent',
        'object': caliper_object
    })

    caliper_event['referrer'].update({
        'id': current_event['referer'],
        'type': 'WebPage'
    })

    caliper_event['actor'].update({
        'name': current_event['username'],
        'type': 'Person'
    })

    caliper_event['extensions']['extra_fields'].update(current_event['context'])
    caliper_event['extensions']['extra_fields']['ip'] = current_event['ip']
    caliper_event['extensions']['extra_fields'].pop('session')
    return caliper_event


def edx_drag_and_drop_v2_loaded(current_event, caliper_event):
    """
    The server emits this event after a drag and drop problem is shown in the LMS.


    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """

    caliper_object = {
        'id': current_event['referer'],
        'type': 'AssessmentItem'
    }

    caliper_event.update({
        'action': 'Viewed',
        'type': 'ViewEvent',
        'object': caliper_object
    })

    caliper_event['referrer'].update({
        'id': current_event['referer'],
        'type': 'WebPage'
    })

    caliper_event['actor'].update({
        'name': current_event['username'],
        'type': 'Person'
    })

    caliper_event['extensions']['extra_fields'].update(current_event['context'])
    caliper_event['extensions']['extra_fields']['ip'] = current_event['ip']
    caliper_event['extensions']['extra_fields'].pop('session')
    return caliper_event
