from openedx.features.caliper_tracking.transformers.bookmark_transformers import edx_bookmark_listed


"""Mapping of events to their transformer functions
"""
EVENT_MAPPING = {
    'edx.bookmark.listed': edx_bookmark_listed,
}
