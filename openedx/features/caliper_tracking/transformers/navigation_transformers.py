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
        'type': 'NavigationEvent',
        'action': 'NavigatedTo',
        'object': caliper_object,
    })

    caliper_event['extensions']['extra_fields'].update({
        'event': current_event['event'],
        'ip': current_event['ip'],
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


def edx_ui_lms_sequence_previous_selected(current_event, caliper_event):
    """
    This event is generated when the user presses the previous button to
    traverse over unit of the previous chapter.

    :param current_event: default logs generated by edx itself
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """
    caliper_object = {
        'id': current_event['referer'],
        'type': 'WebPage',
        'extensions': json.loads(current_event['event'])
    }

    caliper_event.update({
        'type': 'NavigationEvent',
        'action': 'NavigatedTo',
        'object': caliper_object,
    })

    caliper_event['extensions']['extra_fields'].update({
        'ip': current_event['ip'],
        'course_id': current_event['context']['course_id']
    })

    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })

    caliper_event['referrer']['type'] = 'WebPage'

    return caliper_event


def edx_ui_lms_sequence_next_selected(current_event, caliper_event):
    """
    This event is generated when the user presses the next button to traverse
    over unit of next chapter.

    :param current_event: default logs generated by edx itself
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """
    caliper_object = {
        'id': current_event['referer'],
        'type': 'WebPage',
        'extensions': json.loads(current_event['event'])
    }

    caliper_event.update({
        'type': 'NavigationEvent',
        'action': 'NavigatedTo',
        'object': caliper_object,
    })

    caliper_event['extensions']['extra_fields'].update({
        'ip': current_event['ip'],
        'course_id': current_event['context']['course_id']
    })

    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })

    caliper_event['referrer']['type'] = 'WebPage'

    return caliper_event


def seq_next(current_event, caliper_event):
    """
    This event is generated when the user presses the next button to traverse
    over next unit of same chapter.

    :param current_event: default logs generated by edx itself
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """
    caliper_object = {
        'id': current_event['referer'],
        'type': 'WebPage',
        'extensions': json.loads(current_event['event'])
    }

    caliper_event.update({
        'type': 'NavigationEvent',
        'action': 'NavigatedTo',
        'object': caliper_object,
    })

    caliper_event['extensions']['extra_fields'].update({
        'ip': current_event['ip'],
        'event_source': current_event['event_source'],
        'course_id': current_event['context']['course_id'],
        'name': current_event['name']
    })

    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })

    caliper_event['referrer']['type'] = 'WebPage'

    return caliper_event


def seq_prev(current_event, caliper_event):
    """
    This event is generated when the user presses the previous button to
    traverse over previous unit of same chapter.

    :param current_event: default logs generated by edx itself
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """
    caliper_object = {
        'id': current_event['referer'],
        'type': 'WebPage',
        'extensions': json.loads(current_event['event'])
    }

    caliper_event.update({
        'type': 'NavigationEvent',
        'action': 'NavigatedTo',
        'object': caliper_object,
    })

    caliper_event['extensions']['extra_fields'].update({
        'ip': current_event['ip'],
        'event_source': current_event['event_source'],
        'course_id': current_event['context']['course_id'],
        'name': current_event['name']
    })

    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })

    caliper_event['referrer']['type'] = 'WebPage'

    return caliper_event


def edx_course_student_notes_notes_page_viewed(current_event, caliper_event):
    """
    This event is generated when the user presses the notes button to see
    notes made on that course.

    :param current_event: default logs generated by edx itself
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """
    caliper_object = {
        'id': current_event['referer'],
        'type': 'WebPage',
        'extensions': json.loads(current_event['event'])
    }

    caliper_object['extensions'].update({
        'course_id': current_event['context']['course_id'],
        'org_id': caliper_event['extensions']['extra_fields'].pop('org_id')
    })

    caliper_event.update({
        'type': 'NavigationEvent',
        'action': 'NavigatedTo',
        'object': caliper_object,
    })

    caliper_event['extensions']['extra_fields'].update({
        'ip': current_event['ip'],
        'event_source': current_event['event_source']
    })

    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })

    caliper_event['referrer']['type'] = 'WebPage'

    return caliper_event


def seq_goto(current_event, caliper_event):
    """
    This event is generated when the user presses the previous button to traverse
    over previous unit of same chapter.

    :param current_event: default logs generated by edx itself
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """
    caliper_object = {
        'id': current_event['referer'],
        'type': 'Page',
        'extensions': json.loads(current_event['event'])
    }

    caliper_event.update({
        'type': 'NavigationEvent',
        'action': 'NavigatedTo',
        'object': caliper_object,
    })

    caliper_event['extensions']['extra_fields'].update({
        'ip': current_event['ip'],
        'course_id': current_event['context']['course_id'],
        'name': current_event['name']
    })

    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })

    caliper_event['referrer']['type'] = 'WebPage'

    return caliper_event
