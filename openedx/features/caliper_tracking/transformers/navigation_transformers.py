"""
Transformers for all the navigation events
"""

import json


def edx_ui_lms_link_clicked(current_event, caliper_event):
    """
    This trannsformer uses current_event to generate caliper_event
    with currently available data.

    :param current_event: default event log generated.
    :param caliper_event: caliper_event log having some basic attributes.
    :return: updated caliper_event.
    """
    return current_event
