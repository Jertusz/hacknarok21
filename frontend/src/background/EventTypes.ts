enum ALL_EVENTS {
    ANSWER_RANDOM_QUESTION = 'activity_question_answered',
    ANSWER_TEACHERS_QUESTION = 'custom_question_answered',
    TEACHER_QUESTION_APPEARS = 'custom_question_asked',
    RANDOM_QUESTION_APPEARS = 'show_activity_question',
    QUESTION_TIMEOUT = 'hide',
    GENERIC_EVENT = 'generic',
}
enum ADMIN_SENDABLE_EVENTS {
    TEACHER_QUESTION_APPEARS = 'custom_question_asked',
    RANDOM_QUESTION_APPEARS = 'show_activity_question',
    QUESTION_TIMEOUT = 'hide',
}
enum USER_SENDABLE_EVENTS {
    ANSWER_RANDOM_QUESTION = 'activity_question_answered',
    ANSWER_TEACHERS_QUESTION = 'custom_question_answered',
}
enum GENERIC_EVENTS {
    TAB_SWITCHED = 'TAB_SWITCHED',
    WINDOW_SWITCHED = 'WINDOW_SWITCHED',
    LEFT_SESSION = "LEFT_SESSION",
    JOINED_SESSION = "JOINED_SESSION",
    MOUSE_INACTIVE = "MOUSE_INACTIVE"
}
export { ALL_EVENTS, ADMIN_SENDABLE_EVENTS, USER_SENDABLE_EVENTS, GENERIC_EVENTS };
