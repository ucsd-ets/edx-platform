"""
Transformers for all openassessment events
"""
from openedx.features.caliper_tracking.utils import convert_datetime


def openassessmentblock_peer_assess(current_event, caliper_event):
    """
    The server emits this event when a learner submits an assessment of peer's response.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """
    caliper_event.update({
        'type': 'AssessmentEvent',
        'action': 'Submitted',
        'object': {
            'id': current_event['referer'],
            'type': 'Assessment',
            'extensions': {
                'feedback': current_event['event']['feedback'],
                'parts': current_event['event']['parts'],
                'rubric': current_event['event']['rubric'],
                'score_type': current_event['event']['score_type'],
                'scored_at': convert_datetime(current_event['event']['scored_at']),
                'scorer_id': current_event['event']['scorer_id'],
                'submission_uuid': current_event['event']['submission_uuid']
            }
        }
    })
    caliper_event['extensions']['extra_fields'].update({
        'asides': current_event['context']['asides'],
        'course_id': current_event['context']['course_id'],
        'course_user_tags': current_event['context']['course_user_tags'],
        'module': current_event['context']['module']
    })
    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })
    caliper_event['referrer']['type'] = 'WebPage'
    caliper_event['extensions']['extra_fields']['ip'] = current_event['ip']
    caliper_event['extensions']['extra_fields'].pop('session')
    return caliper_event
