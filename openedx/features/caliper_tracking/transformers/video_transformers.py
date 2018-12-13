"""
Transformers for all the video events
"""

import json
from datetime import timedelta

from isodate import duration_isoformat


def pause_video(current_event, caliper_event):
    """
    When a user selects the video player's pause control, the player emits a
    pause_video event. Fot videos that are streamed in a browser, when the
    player reaches the end of the video file and play automatically stops it
     emits both this event and a stop event (as of June 2014).

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """
    current_event_details = json.loads(current_event['event'])
    caliper_event.update({
        'action': 'Paused',
        'type': 'MediaEvent',
        'object': {
            'duration': duration_isoformat(
                timedelta(seconds=current_event_details['duration'])),
            'extensions': {
                'code': current_event_details['code'],
                'id': current_event_details['id']
            },
            'id': current_event['referer'],
            'type': 'VideoObject'
        },
        'target': {
            'currentTime': duration_isoformat(
                timedelta(seconds=current_event_details['currentTime'])),
            'id': current_event['referer'],
            'type': 'MediaLocation'
        }
    })
    caliper_event['actor'].update({
        'name': current_event['username'],
        'type': 'Person'
    })
    caliper_event['extensions']['extra_fields'].update({
        'course_id': current_event['context']['course_id'],
        'ip': current_event['ip']
    })
    caliper_event['referrer']['type'] = 'WebPage'
    return caliper_event


def edx_video_speed_changed(current_event, caliper_event):
    """
    When the speed of the video is changed.

    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """
    caliper_event.update({
        'action': 'ChangedSpeed',
        'type': 'MediaEvent'
    })
    caliper_event['extensions']['extra_fields'].update({
        'course_id': current_event['context'].get('course_id'),
        'ip': current_event.get('ip')
    })
    caliper_event['referrer']['type'] = 'WebPage'
    caliper_event['actor'].update({
        'name': current_event.get('username'),
        'type': 'Person'
    })
    event_info = json.loads(current_event['event'])
    caliper_event['object'] = {
        'id': current_event.get('referer'),
        'type': 'VideoObject',
        'duration': duration_isoformat(
            timedelta(seconds=event_info.pop('duration'))),
        'extensions': event_info
    }
    return caliper_event
