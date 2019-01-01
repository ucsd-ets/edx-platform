import json
from openedx.features.caliper_tracking import utils
from django.conf import settings
from django.core.urlresolvers import reverse


def edx_team_page_viewed(current_event, caliper_event):
    """
    When a user views any page with a unique URL under the Teams page in the
    courseware, the browser emits an edx.team.page_viewed event.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """

    current_event_details = json.loads(current_event['event'])

    caliper_object = {
        'id': current_event['page'],
        'type': 'WebPage',
        'extensions': current_event_details
    }

    caliper_event.update({
        'type': 'ViewEvent',
        'action': 'Viewed',
        'object': caliper_object
    })

    caliper_event['extensions']['extra_fields'].update({
        'ip': current_event['ip'],
        'course_id': current_event['context']['course_id'],
    })

    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })

    caliper_event['referrer']['type'] = 'WebPage'

    return caliper_event


def edx_team_learner_added(current_event, caliper_event):
    """
    When a user joins a team or is added by someone else,
    the server emits an edx.team.learner_added event.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """
    username = utils.get_username_from_user_id(current_event['event']['user_id'])

    user_link = '{lms_url}{profile_link}'.format(
        lms_url=settings.LMS_ROOT_URL,
        profile_link=str(reverse(
            'learner_profile',
            kwargs={'username': username}
        ))
    )

    object_link = utils.get_team_url_from_team_id(current_event['referer'], current_event['event']['team_id'])

    caliper_object = {
        'id': object_link,
        'member': {
            'extensions': {
                'user_id': current_event['event']['user_id']
            },
            'id': user_link,
            'name': username,
            'type': 'Person'
        },
        'organization': {
            'extensions': {
                'team_id': current_event['event']['team_id']
            },
            'id': object_link,
            'type': 'Group'
        },
        'type': 'Membership',
        'extensions': {
            'add_method': current_event['event']['add_method']
        }
    }

    caliper_event.update({
        'type': 'Event',
        'action': 'Added',
        'object': caliper_object,
    })

    caliper_event['actor'].update({
        'type': 'Person',
        'name': current_event['username']
    })

    caliper_event['referrer'].update({
        'type': 'WebPage'
    })

    caliper_event['extensions']['extra_fields'].update({
        'ip': current_event['ip'],
        'course_id': current_event['context']['course_id'],
    })

    return caliper_event


def edx_team_changed(current_event, caliper_event):
    """
    This event is generated when user edits any field in a team.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """

    object_extensions = current_event['event']

    object_link = utils.get_team_url_from_team_id(current_event['referer'],
                                                  current_event['event'][
                                                      'team_id'])
    object_extensions.update({
        'course_id': current_event['context']['course_id'],
        'org_id': caliper_event['extensions']['extra_fields'].pop('org_id'),
    })

    caliper_object = {
        'id': object_link,
        'type': 'Group',
        'extensions': object_extensions
    }

    caliper_event.update({
        'type': 'Event',
        'action': 'Modified',
        'object': caliper_object
    })

    caliper_event['referrer']['type'] = 'WebPage'

    caliper_event['actor'].update({
        'name': current_event['username'],
        'type': 'Person'
    })

    caliper_event['extensions']['extra_fields'].update({
        'ip': current_event['ip'],
    })

    return caliper_event
