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
    'stop_video': ctf.stop_video,
    'problem_graded': ctf.problem_graded,
    'problem_save': ctf.problem_save,
    'edx.problem.hint.demandhint_displayed':
        ctf.edx_problem_hint_demandhint_displayed,
    'pause_video': ctf.pause_video,
    'seek_video': ctf.seek_video,
    'load_video': ctf.load_video,
    'edx.video.closed_captions.hidden': ctf.edx_video_closed_caption_hidden,
    'problem_reset': ctf.problem_reset,
    'problem_rescore': ctf.problem_rescore,
    'edx.forum.thread.viewed': ctf.edx_forum_thread_viewed,
    'save_problem_success': ctf.save_problem_success,
    'play_video': ctf.play_video,
    'edx.forum.thread.created': ctf.edx_forum_thread_created,
    'openassessmentblock.peer_assess': ctf.openassessmentblock_peer_assess,
    'edx.forum.comment.created': ctf.edx_forum_comment_created,
    'problem_check': ctf.problem_check,
    'openassessmentblock.create_submission': ctf.openassessmentblock_create_submission,
    'xblock.poll.submitted': ctf.xblock_poll_submitted,
    'edx.course.student_notes.added': ctf.edx_course_student_notes_added,
    'openassessmentblock.get_submission_for_staff_grading': ctf.openassessmentblock_get_submission_for_staff_grading,
}
