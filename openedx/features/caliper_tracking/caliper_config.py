from openedx.features.caliper_tracking.transformers.bookmark_transformers import edx_bookmark_listed
from openedx.features.caliper_tracking.transformers.enrollment_transformers import edx_course_enrollment_activated

"""
Mapping of events to their transformer functions
"""

EVENT_MAPPING = {
    'edx.bookmark.listed': edx_bookmark_listed,
    'edx.course.enrollment.activated': edx_course_enrollment_activated,
}
