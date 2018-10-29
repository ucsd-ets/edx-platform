"""
Base module containing generic caliper transformer class
"""


import uuid

class CaliperBaseTransformer(object):
    """Base transformer class

    This class is responsible for adding all the caliper compliant
    fields which are common to all events
    """
    def __init__(self, event):
        """Constructor

        Adds all of the generic fields to the event object

        @param event: unprocessed event dict
        """
        self.event = event
        self.caliper_event = event
        self.caliper_event['uuid'] = str(uuid.uuid4().urn)

    def transform_event(self):
        return self.caliper_event
