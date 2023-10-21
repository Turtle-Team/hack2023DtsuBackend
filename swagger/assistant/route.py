import json
import mimetypes

import flask

import database.handler
import database.processor

import swagger.assistant.models
import swagger.assistant.gpt
import swagger.mimetype
from swagger.assistant.namespace import assistant
import flask_restplus
import flask_app
import swagger.mimetype


@assistant.route('/quest', methods=['POST'])
class NewUser(flask_restplus.Resource):

    @assistant.expect(swagger.assistant.models.REQUEST_ASSISTANT)
    def post(self):
        data = flask.request.json
        if not data.get('text'):
            return
        answer = swagger.assistant.gpt.GPTAssitant().send_quest(data.get('text'))
        json_answer = json.dumps({"answer": answer}, ensure_ascii=False)
        return flask_app.app.response_class(response=json_answer, mimetype=swagger.mimetype.APP_JSON)

