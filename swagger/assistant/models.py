import swagger.assistant.namespace
import flask_restplus

REQUEST_ASSISTANT = swagger.assistant.namespace.assistant.model(
    "ASSISTANT_QUEST",
    {
        "text": flask_restplus.fields.String(description="text", required=True),
    },
)


