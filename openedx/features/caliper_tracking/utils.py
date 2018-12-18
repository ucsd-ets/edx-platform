"""
Utils required in transformers
"""
from dateutil.parser import parse
from django.contrib.auth import get_user_model

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
