import json
from datetime import datetime

from django.test import TestCase
import logging

from openedx.features.caliper_tracking.base_transformer import CaliperBaseTransformer
from openedx.features.caliper_tracking.caliper_config import EVENT_MAPPING


LOGGER = logging.getLogger(__name__)
TEST_DIR_PATH = 'openedx/features/caliper_tracking/tests/'


class BaseTransformerTestCase(TestCase):
    """docstring for  BaseTransformerTestCase"""

    base_event = {
        'username': 'honor',
        'event_source': 'server',
        'name': 'edx.course.enrollment.activated',
        'accept_language': 'en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7',
        'time': '2018-10-17T12:12:03.143959+00:00',
        'agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'page': None,
        'host': '747befdb3d9d',
        'session': '8205ce7ea40a0619955e15f072dc33e2',
        'referer': 'http://localhost:18000/courses/course-v1:edx+cs-101+2018/about',
        'context': {
            'user_id': 6,
            'org_id': 'edx',
            'course_id': 'course-v1:edx+cs-101+2018',
            'path': '/change_enrollment'
        },
        'ip': '172.18.0.1',
        'event': {
            'course_id': 'course-v1:edx+cs-101+2018',
            'user_id': 6,
            'mode': 'audit'
        },
        'event_type': 'edx.course.enrollment.activated'
    }

    def stuff(self):
        caliper_event = CaliperBaseTransformer(
            self.base_event).transform_event()

        self.assertIn('@context', caliper_event)
        self.assertIn('id', caliper_event)
        self.assertIn('eventTime', caliper_event)
        self.assertIn('actor', caliper_event)
        self.assertIn('id', caliper_event['actor'])

        self.assertEqual(caliper_event.get('agent'),
                         self.base_event.get('agent'))
        self.assertEqual(caliper_event.get('edx_event_type'),
                         self.base_event.get('event_type'))
        self.assertEqual(caliper_event.get('host'),
                         self.base_event.get('host'))
        self.assertEqual(caliper_event.get('session'),
                         self.base_event.get('session'))
        self.assertEqual(caliper_event.get('referer'),
                         self.base_event.get('referer'))
        self.assertEqual(caliper_event.get('user_id'),
                         self.base_event['context'].get('user_id'))
        self.assertEqual(caliper_event.get('org_id'),
                         self.base_event['context'].get('org_id'))
        self.assertEqual(caliper_event.get('course_id'),
                         self.base_event['context'].get('course_id'))
        self.assertEqual(caliper_event.get('path'),
                         self.base_event['context'].get('path'))

    def test_my_func(self):

        input_file = '{}before/{}'.format(
            TEST_DIR_PATH,
            'edx.course.enrollment.activated.json'
        )
        output_file = '{}after/{}'.format(
            TEST_DIR_PATH,
            'edx.course.enrollment.activated.json'
        )

        with open(input_file) as before, open(output_file) as after:
            event = json.loads(before.read())
            expected_event = json.loads(after.read())

            caliper_event = CaliperBaseTransformer(event).transform_event()
            related_function = EVENT_MAPPING[event.get('event_type')]
            caliper_event =  related_function(event, caliper_event)

            self.assertEqual(caliper_event, expected_event)


