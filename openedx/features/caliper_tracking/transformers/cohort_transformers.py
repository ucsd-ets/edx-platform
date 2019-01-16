"""
Transformers for all cohort related events.
"""

from django.conf import settings
from django.core.urlresolvers import reverse

from openedx.features.caliper_tracking import utils


def edx_cohort_user_added(current_event, caliper_event):
    """
    When new user is added to cohort.

    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """

    username = utils.get_username_from_user_id(
        current_event['event']['user_id'])

    cohort_page_link = '{instructor_page}#view-cohort_management'.format(
        instructor_page=current_event['referer'])

    user_link = '{lms_url}{profile_link}'.format(
        lms_url=settings.LMS_ROOT_URL,
        profile_link=str(reverse(
            'learner_profile',
            kwargs={'username': username}
        ))
    )

    caliper_object = {
        'id': cohort_page_link,
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
                'cohort_id': current_event['event']['cohort_id']
            },
            'id': cohort_page_link,
            'name': current_event['event']['cohort_name'],
            'type': 'Group'
        },
        'type': 'Membership'
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
        'course_user_tags': current_event['context']['course_user_tags']
    })

    return caliper_event


def edx_cohort_created(current_event, caliper_event):
    """
    Server emits edx.cohort.created event when new cohort is created.

    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """

    cohort_page_link = '{instructor_page}#view-cohort_management'.format(
        instructor_page=current_event['referer'])

    caliper_object = {
        'extensions': {
            'cohort_id': current_event['event']['cohort_id']
        },
        'id': cohort_page_link,
        'name': current_event['event']['cohort_name'],
        'type': 'Group'
    }

    caliper_event.update({
        'type': 'Event',
        'action': 'Created',
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
        'course_user_tags': current_event['context']['course_user_tags']
    })

    return caliper_event


def edx_cohort_user_removed(current_event, caliper_event):
    """
    When user is removed from cohort.

    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """

    username = utils.get_username_from_user_id(
        current_event['event']['user_id'])

    user_link = '{lms_url}{profile_link}'.format(
        lms_url=settings.LMS_ROOT_URL,
        profile_link=str(reverse(
            'learner_profile',
            kwargs={'username': username}
        ))
    )

    cohort_page_link = '{instructor_page}#view-cohort_management'.format(
        instructor_page=current_event['referer'])

    caliper_object = {
        'id': cohort_page_link,
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
                'cohort_id': current_event['event']['cohort_id']
            },
            'id': cohort_page_link,
            'name': current_event['event']['cohort_name'],
            'type': 'Group'
        },
        'type': 'Membership'
    }

    caliper_event.update({
        'type': 'Event',
        'action': 'Removed',
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
        'course_user_tags': current_event['context']['course_user_tags']
    })

    return caliper_event


def edx_cohort_creation_requested(current_event, caliper_event):
    """
    When a course team member manually creates a cohort on the Cohorts page of the instructor
    dashboard, the server emits an edx.cohort.creation_requested event.

    :param current_event: default log
    :param caliper_event: log containing both basic and default attribute
    :return: final created log
    """

    cohort_page_link = '{instructor_page}#view-cohort_management'.format(
        instructor_page=current_event['referer'])

    caliper_object = {
        'extensions': {
            'cohort_id': current_event['event']['cohort_id']
        },
        'id': cohort_page_link,
        'name': current_event['event']['cohort_name'],
        'type': 'Group'
    }

    caliper_event.update({
        'type': 'Event',
        'action': 'Created',
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
