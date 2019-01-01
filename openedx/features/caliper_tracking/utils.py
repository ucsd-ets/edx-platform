"""
Utils required in transformers
"""
from dateutil.parser import parse
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.urlresolvers import reverse

UTC_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'


def convert_datetime(current_datetime):
    """
    Convert provided datetime into UTC format
    @param datetime: datetime string.
    :return: UTC formatted datetime string.
    """

    # convert current_datetime to a datetime object if it is string
    if type(current_datetime) in (str, unicode):
        current_datetime = parse(current_datetime)

    utc_offset = current_datetime.utcoffset()
    utc_datetime = current_datetime - utc_offset

    formatted_datetime = '{}{}'.format(
        utc_datetime.strftime(UTC_DATETIME_FORMAT)[:-3], 'Z'
    )
    return formatted_datetime


def get_username_from_user_id(user_id):
    """
    @param : user_id
    :return: username from the given user_id.
    """

    User = get_user_model()
    user = User.objects.get(id=user_id)
    return str(user.username)


def get_user_link_from_username(username):
    return '{lms_url}{profile_link}'.format(
        lms_url=settings.LMS_ROOT_URL,
        profile_link=str(reverse(
            'learner_profile',
            kwargs={'username': username}
        ))
    )


def get_topic_id_from_team_id(team_id):
    """
    :param team_id: extracting from event logs
    :return: topic_id for making team url
    """
    from lms.djangoapps.teams.models import CourseTeam
    user_team = CourseTeam.objects.get(team_id=team_id)

    return user_team.topic_id


def get_team_url_from_team_id(referer, team_id):
    """
    :param referer: extract from event logs
    :param team_id: extract from event logs
    :return: team url
    """
    topic_id = get_topic_id_from_team_id(team_id)
    object_link = '{referrer}#teams/{topic_id}/{team_id}'.format(
        referrer=referer,
        topic_id=topic_id,
        team_id=team_id
    )
    return object_link
