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
    
    caliper_event['type'] = 'NavigationEvent'
    caliper_event['action'] = 'NavigateTo'
    caliper_event['actor']['type'] = 'Person'

    # 'event' attribute in current_event has json dumped data. So to obtain
    # target_url , convert it into json object.
    current_event_details = json.loads(current_event['event'])

    caliper_event['object'] = {
        'id': current_event_details['target_url'],
        'type': 'WebPage',
    }

    return caliper_event
