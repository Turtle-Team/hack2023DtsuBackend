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
        result = str(json_quizis)
        return flask_app.app.response_class(response=result, mimetype=swagger.mimetype.APP_JSON)


@quiz.route('/accept_answer', methods=['POST'])
class PostNiceQuiz(flask_restplus.Resource):
    @quiz.expect(swagger.quiz.models.QUIZ_NICE_ANSWER)
    def post(self):
        data = flask.request.json
        if not data.get('login') and not data.get('quiz_id'):
            return flask_app.app.response_class(status=500)
        nice_data = (data.get('login'), data.get('quiz_id'))
        database.handler.Db().insert_new_answer(*nice_data)

        return flask_app.app.response_class(status=200, response=str({'result': True}), mimetype=swagger.mimetype.APP_JSON)

@quiz.route('/get_user_point', methods=['GET'])
class GetCurrentUserPoint(flask_restplus.Resource):
    @quiz.doc(params={'login': 'Логин пользователя с приложения'})
    def get(self):
        data = flask.request.args.get('login')
        if not data:
            return flask_app.app.response_class(status=500)
        db_result = database.handler.Db().select_user_answer(data)
        points = 0
        for i in db_result:
            if i[2] == 1:
                points += 1
        return flask_app.app.response_class(status=200, response=str({"login": data,'points': points}), mimetype=swagger.mimetype.APP_JSON)
