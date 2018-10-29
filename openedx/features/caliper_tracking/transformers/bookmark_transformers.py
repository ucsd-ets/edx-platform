"""
Transformers for all the bookmark events
"""


def edx_bookmark_listed(current_event, caliper_event):
    caliper_event = current_event
    return caliper_event


def edx_bookmark_added(current_event, caliper_event):
    print('edx_bookmark_added')


def edx_bookmark_accessed(current_event, caliper_event):
    print('edx_bookmark_accessed')


def edx_bookmark_removed(current_event, caliper_event):
    print('edx_bookmark_removed')


def edx_course_tool_accessed(current_event, caliper_event):
    print('edx_course_tool_accessed')
