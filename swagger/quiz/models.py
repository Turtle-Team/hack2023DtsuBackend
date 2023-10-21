import swagger.quiz.namespace
import flask_restplus


QUIZ_NICE_ANSWER = swagger.quiz.namespace.quiz.model(
    "QUIZ_NICE_ANSWER",
    {
        "login": flask_restplus.fields.String(description="elyadskiy", required=True),
        "quiz_id": flask_restplus.fields.Integer(description="0", required=True),
    },
)