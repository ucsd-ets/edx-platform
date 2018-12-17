from openedx.features.caliper_tracking import transformers as ctf

"""
Mapping of events to their transformer functions
"""

EVENT_MAPPING = {
    'edx.bookmark.added': ctf.edx_bookmark_added,
    'edx.bookmark.listed': ctf.edx_bookmark_listed,
    'edx.bookmark.accessed': ctf.edx_bookmark_accessed,
    'edx.bookmark.removed': ctf.edx_bookmark_removed,
    'edx.ui.lms.link_clicked': ctf.edx_ui_lms_link_clicked,
    'edx.course.enrollment.activated': ctf.edx_course_enrollment_activated,
    'edx.course.enrollment.deactivated': ctf.edx_course_enrollment_deactivated,
    'edx.course.enrollment.mode_changed':
        ctf.edx_course_enrollment_mode_changed,
    'edx.course.enrollment.upgrade.clicked':
        ctf.edx_course_enrollment_upgrade_clicked,
    'speed_change_video': ctf.edx_video_speed_changed,
    'edx.course.tool.accessed': ctf.edx_course_tool_accessed,
    'edx.forum.response.created': ctf.edx_forum_response_created,
    'problem_show': ctf.problem_show,
    'edx.ui.lms.sequence.next_selected': ctf.edx_ui_lms_sequence_next_selected,
    'edx.ui.lms.sequence.previous_selected':
        ctf.edx_ui_lms_sequence_previous_selected,
    'seq_next': ctf.seq_next,
    'seq_prev': ctf.seq_prev,
    'problem_save': ctf.problem_save,
    'pause_video': ctf.pause_video,
    'problem_reset': ctf.problem_reset,
    'edx.forum.thread.created': ctf.edx_forum_thread_created,
    'edx.forum.comment.created': ctf.edx_forum_comment_created,
}
