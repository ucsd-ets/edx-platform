"""
Base module containing generic caliper transformer class
"""
import uuid
from datetime import datetime

from django.conf import settings
from django.core.urlresolvers import reverse

CALIPER_EVENT_CONTEXT = 'http://purl.imsglobal.org/ctx/caliper/v1p1'


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
        self.caliper_event = dict()
        self.add_generic_fields()
        self.add_actor_info()

    def add_generic_fields(self):
        """
        Adds all of the generic fields to the event object
        """
        self.caliper_event.update({
            '@context': CALIPER_EVENT_CONTEXT,
            'id': str(uuid.uuid4().urn),
            'agent': self.event.get('agent'),
            'edx_event_type': self.event.get('event_type'),
            'host': self.event.get('host'),
            'session': self.event.get('session'),
            'referrer': self.event.get('referer'),
            'user_id': self.event['context'].get('user_id'),
            'org_id': self.event['context'].get('org_id'),
            'path': self.event['context'].get('path'),
            'eventTime': datetime.now().isoformat('T')
        })

    def add_actor_info(self):
        self.caliper_event['actor'] = dict()
        user_profile_link = '{lms_url}{profile_link}'.format(
            lms_url=settings.LMS_BASE,
            profile_link=str(reverse('learner_profile', kwargs={'username': self.event.get('username')}))
        )
        self.caliper_event['actor'].update({
            'id': user_profile_link,
        })

    def transform_event(self):
        return self.caliper_event
