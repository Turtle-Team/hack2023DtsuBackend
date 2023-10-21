import json
import mimetypes

import flask

import database.handler
import database.processor

import swagger.quiz.models
from swagger.quiz.namespace import quiz
import flask_restplus
import flask_app
import swagger.mimetype


@quiz.route('/get', methods=['GET'])
class GetQuiz(flask_restplus.Resource):

    def get(self):
        quizis = database.processor.DataProcessor().get_quiz_all()
        json_quizis = []
        for i in quizis:
            json_quizis.append(i.to_json())
        json_data = json.dumps(json_quizis, ensure_ascii=False)
        return flask_app.app.response_class(response=json_data, mimetype=swagger.mimetype.APP_JSON)
