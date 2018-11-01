from openedx.features.caliper_tracking.transformers.bookmark_transformers import edx_bookmark_listed
from openedx.features.caliper_tracking.transformers.enrollment_transformers import edx_course_enrollment_activated
from openedx.features.caliper_tracking.transformers.navigation_transformers import edx_ui_lms_link_clicked

"""
Mapping of events to their transformer functions
"""

EVENT_MAPPING = {
    'edx.bookmark.listed': edx_bookmark_listed,
    'edx.ui.lms.link_clicked': edx_ui_lms_link_clicked,
    'edx.course.enrollment.activated': edx_course_enrollment_activated,
}
