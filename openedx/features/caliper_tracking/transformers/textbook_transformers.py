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


def textbook_pdf_search_executed(current_event, caliper_event):
    """
    The browser emits textbook.pdf.search.executed events when
    a user searches for a text value in the file.

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
        'action': 'Searched',
        'type': 'Event',
        'object': caliper_event_object
    })

    return caliper_event


def textbook_pdf_page_navigated(current_event, caliper_event):
    """
    The browser emits textbook.pdf.page.navigated events when a
    user manually enters a page number.

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

    caliper_event_object = {
        'id': current_event['referer'],
        'type': 'Document',
        'extensions': {
                'chapter': current_event_details['chapter'],
                'page': current_event_details['page']
        }
    }

    caliper_event.update({
        'action': 'NavigatedTo',
        'type': 'NavigationEvent',
        'object': caliper_event_object
    })

    return caliper_event


def textbook_pdf_zoom_menu_changed(current_event, caliper_event):
    """
    The browser emits textbook.pdf.zoom.menu.changed events when
    a user selects a magnification setting.

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

    caliper_event_object = {
        'id': current_event['referer'],
        'type': 'Document',
        'extensions': current_event_details
    }
    caliper_event.update({
        'action': 'ChangedSize',
        'type': 'Event',
        'object': caliper_event_object
    })
    return caliper_event


def book(current_event, caliper_event):
    """
    The browser emits book events when a user navigates within the PDF
    Viewer or the PNG Viewer.

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


def textbook_pdf_thumbnail_navigated(current_event, caliper_event):
    """
    The browser emits textbook.pdf.thumbnail.navigated events when a user clicks on a thumbnail image to
    navigate to a page.

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


def textbook_pdf_zoom_buttons_changed(current_event, caliper_event):
    """
    The browser emits textbook.pdf.zoom.buttons.changed events when
    a user clicks either the Zoom In or Zoom Out icon.

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

    caliper_event_object = {
        'id': current_event['referer'],
        'type': 'Document',
        'extensions': current_event_details
    }
    caliper_event.update({
        'action': 'ChangedSize',
        'type': 'Event',
        'object': caliper_event_object
    })
    return caliper_event


def textbook_pdf_searchcasesensitivity_toggled(current_event, caliper_event):
    """
    The browser emits textbook.pdf.searchcasesensitivity.toggled events when a
    user selects or clears the Match Case option for a search.

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

    caliper_event_object = {
        'id': current_event['referer'],
        'type': 'SoftwareApplication',
        'extensions': current_event_details
    }

    caliper_event.update({
        'action': 'Used',
        'type': 'ToolUseEvent',
        'object': caliper_event_object
    })

    return caliper_event
