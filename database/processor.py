import json
import typing

import database.handler
import database.obj

class DataProcessor:
    def __init__(self):
        self.handler = database.handler.Db()
    def get_quiz_all(self):
        alL_quiz_list = self.handler.select_quiz_all()
        convert_list_quiz: typing.List[database.obj.Quiz] = []
        for i in alL_quiz_list:
            answer_this_quiz = self.handler.select_answer_by_quiz_id(i[0])
            answer_list: typing.List[database.obj.Quiz.answers] = []
            for j in answer_this_quiz:
                answer_list.append(database.obj.Answer(j[0], j[2], j[3]))
            convert_list_quiz.append(database.obj.Quiz(i[0], i[1], answer_list))
        return convert_list_quiz

    def __del__(self):
        del self.handler
