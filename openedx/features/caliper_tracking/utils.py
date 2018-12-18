"""
Utils required in transformers
"""
from dateutil.parser import parse

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
