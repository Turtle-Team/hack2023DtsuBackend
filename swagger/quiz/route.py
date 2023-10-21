import json
import mimetypes

import flask

from database.processor import DataProcessor
import database.processor

import swagger.quiz.models
from swagger.quiz.namespace import quiz
import flask_restplus
import flask_app
import swagger.mimetype
import settings
import mysql.connector


class Questions:
    def __init__(self):
        self.connection = mysql.connector.connect(user=settings.DATABASE['login'],
                                                  host=settings.DATABASE['ip'],
                                                  database=settings.DATABASE['basename'],
                                                  password=settings.DATABASE['password'])
        self.cursor = self.connection.cursor()

    def questions(self):
        query = ("SELECT quiz.id_quiz, quiz.name AS quiz_name, answer.id_answer"
                 ", answer.name AS answer_name,"
                 " answer.is_answer FROM quiz INNER JOIN answer ON quiz.quiz_id = answer.id_quiz")
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.connection.close()