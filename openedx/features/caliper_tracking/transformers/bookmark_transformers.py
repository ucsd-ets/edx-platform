"""
Transformers for all the bookmark events
"""


def edx_bookmark_listed(current_event, caliper_event):
    """
    The server emits this event when a user clicks Bookmarks under
    the Course Tools heading in the LMS to view the list of previously
    bookmarked pages. If the number of bookmarks exceeds the defined
    page length, the browser emits an additional edx.course.bookmark.listed
    event each time the user navigates to a different page of results.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """
    caliper_event.update({
        'type': 'NavigationEvent',
        'action': 'NavigatedTo',
        'object': {
            'id': current_event['referer'],
            'type': 'WebPage'
        }
    })

    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })

    caliper_event['referrer'].update({
        'type': 'WebPage'
    })

    caliper_event['extensions']['extra_fields'].update({
        'course_id': current_event['event'].get('course_id'),
        'ip': current_event.get('ip'),
        'page_number': current_event['event'].get('page_number'),
        'bookmarks_count': current_event['event'].get('bookmarks_count'),
        'page_size': current_event['event'].get('page_size'),
        'list_type': current_event['event'].get('list_type'),
    })

    return caliper_event


def edx_bookmark_added(current_event, caliper_event):
    print('edx_bookmark_added')


def edx_bookmark_accessed(current_event, caliper_event):
    print('edx_bookmark_accessed')


def edx_bookmark_removed(current_event, caliper_event):
    print('edx_bookmark_removed')


def edx_course_tool_accessed(current_event, caliper_event):
    print('edx_course_tool_accessed')
