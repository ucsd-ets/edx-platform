"""
Transformers for all the textbook interaction events
"""
import json


def textbook_pdf_page_scrolled(current_event, caliper_event):
    """
    The browser emits textbook.pdf.page.scrolled events each time the
    displayed page changes while a user scrolls up or down.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """

    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })

    caliper_event['referrer']['type'] = 'WebPage'

    caliper_event['extensions']['extra_fields'].update({
        'course_id': current_event['context'].get('course_id'),
        'ip': current_event['ip'],
    })

    current_event_details = json.loads(current_event['event'])
    current_event_details.pop('name')

    caliper_event_object = {
        'id': current_event['referer'],
        'type': 'Document',
        'extensions': current_event_details
    }
    caliper_event.update({
        'action': 'NavigatedTo',
        'type': 'NavigationEvent',
        'object': caliper_event_object
    })
    return caliper_event
