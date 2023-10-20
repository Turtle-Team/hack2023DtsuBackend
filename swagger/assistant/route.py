import json
import mimetypes

import flask

import database.handler
import database.processor

import swagger.assistant.models
from swagger.assistant.namespace import assistant
import flask_restplus
import flask_app
import swagger.mimetype


@assistant.route('/new', methods=['POST'])
class NewUser(flask_restplus.Resource):

    @assistant.expect(swagger.assistant.models.REQUEST_ASSISTANT)
    def post(self):
        data = flask.request.json
