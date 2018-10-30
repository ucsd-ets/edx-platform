"""
Utils required in transformers
"""
from opaque_keys.edx.locator import CourseLocator
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview


def get_course(course_key):
    # TODO not finalized
    course_id = CourseLocator.from_string(course_key)
    return CourseOverview.objects.get(id=course_id)