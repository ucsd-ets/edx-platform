from functools import wraps

from .processor import CaliperProcessor


def transform_caliper(logging_func):
    """
    Decorator to transform events into caliper transformed events.
    """

    @wraps(logging_func)
    def transform(event):
        caliper_event = None

        if event and '/' not in event['event_type']:
            caliper_event = CaliperProcessor()(event)

        return logging_func(
            caliper_event
            if caliper_event else event
        )

    return transform
