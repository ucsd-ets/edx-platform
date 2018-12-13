from openedx.features.caliper_tracking import transformers as ctf

"""
Mapping of events to their transformer functions
"""

EVENT_MAPPING = {
    'edx.bookmark.added': ctf.edx_bookmark_added,
    'edx.bookmark.listed': ctf.edx_bookmark_listed,
    'edx.bookmark.removed': ctf.edx_bookmark_removed,
    'edx.ui.lms.link_clicked': ctf.edx_ui_lms_link_clicked,
    'edx.course.enrollment.activated': ctf.edx_course_enrollment_activated,
    'edx.course.enrollment.deactivated': ctf.edx_course_enrollment_deactivated,
    'edx.course.enrollment.mode_changed': ctf.edx_course_enrollment_mode_changed,
    'edx.course.enrollment.upgrade.clicked': ctf.edx_course_enrollment_upgrade_clicked,
    'edx.course.tool.accessed': ctf.edx_course_tool_accessed,
    'problem_show': ctf.problem_show,
    'pause_video': ctf.pause_video,
}
