"""
Base module containing generic caliper transformer class
"""
import uuid

from dateutil.parser import parse
from django.conf import settings
from django.core.urlresolvers import reverse

CALIPER_EVENT_CONTEXT = 'http://purl.imsglobal.org/ctx/caliper/v1p1'

UTC_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'


class CaliperBaseTransformer(object):
    """Base transformer class

    This class is responsible for adding all the caliper compliant
    fields which are common to all events
    """

    def __init__(self, event):
        """Constructor

        @param event: unprocessed event dict
        """
        self.event = event
        self.caliper_event = {}
        self._add_generic_fields()
        self._add_actor_info()
        self._add_referrer()
        self._add_extensions()

    def _convert_datetime(self, current_datetime):
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

    def _add_generic_fields(self):
        """
        Adds all of the generic fields to the event object
        """
        self.caliper_event.update({
            '@context': CALIPER_EVENT_CONTEXT,
            'id': uuid.uuid4().urn,
            'eventTime': self._convert_datetime(self.event.get('time'))
        })

    def _add_actor_info(self):
        """
        Adds all generic information related to `actor`
        """
        self.caliper_event['actor'] = {}
        user_profile_link = '{lms_url}{profile_link}'.format(
            lms_url=settings.LMS_ROOT_URL,
            profile_link=str(reverse(
                'learner_profile',
                kwargs={'username': self.event.get('username')}
            ))
        )
        self.caliper_event['actor'].update({
            'id': user_profile_link,
        })

    def _add_extensions(self):
        """
        A map of additional attributes not defined by the model MAY be
        specified for a more concise representation of the Event.
        """
        self.caliper_event['extensions'] = {}
        self.caliper_event['extensions']['extra_fields'] = {
            'agent': self.event.get('agent'),
            'event_type': self.event.get('event_type'),
            'event_source': self.event.get('event_source'),
            'host': self.event.get('host'),
            'org_id': self.event['context'].get('org_id'),
            'path': self.event['context'].get('path'),
            'session': self.event.get('session'),
            'user_id': self.event['context'].get('user_id'),
            'accept_language': self.event.get('accept_language'),
            'page': self.event.get('page'),
        }

    def _add_referrer(self):
        """
        Adds information of an Entity that represents the referring context.
        """
        self.caliper_event['referrer'] = {
            'id': self.event.get('referer')
        }

    def transform_event(self):
        """
        Provides Generic Caliper transformer event.
        :return: Transformed event with basic Caliper standards.
        """
        return self.caliper_event
