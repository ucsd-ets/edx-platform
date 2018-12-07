"""
Transformers for all the navigation events
"""
import json


def edx_ui_lms_link_clicked(current_event, caliper_event):
    """
    This trannsformer uses current_event to generate caliper_event
    with currently available data.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """

    current_event_details = json.loads(current_event['event'])
    caliper_event.update({
        'type': 'NavigationEvent',
        'action': 'NavigatedTo',
        'object': {
            'id': current_event_details['target_url'],
            'type': 'WebPage'
        }
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
        'ip': current_event['ip'],
    })

    return caliper_event


def edx_course_tool_accessed(current_event, caliper_event):
    """
    The browser emits an edx.course.tool.accessed event when a user clicks
    one of the links under the Course Tools heading in the LMS, such
    as Bookmarks, Reviews, or Updates.

    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """
    caliper_object = {
        'id': current_event['page'],
        'type': 'WebPage',
    }

    caliper_event.update({
        'type': 'ToolUseEvent',
        'action': 'Used',
        'object': caliper_object,
    })

    caliper_event['extensions']['extra_fields'].update({
        'event': current_event['event'],
        'ip': current_event['ip'],
        'event_source': current_event['event_source'],
        'course_id': current_event['context']['course_id']
    })

    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })

    caliper_event['referrer'].update({
        'type': 'WebPage'
    })

    return caliper_event
