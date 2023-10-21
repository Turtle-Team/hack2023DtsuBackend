import json
import typing

import database.handler
import database.obj

class DataProcessor:
    def __init__(self):
        self.handler = database.handler.Db()
    def get_all_quiz(self):
        alL_quiz_list = self.handler.select_quiz_all()
        convert_list_quiz: typing.List[database.obj.Quiz] = []
        for i in alL_quiz_list:
            convert_list_quiz.append(database.obj.Quiz(i[0], i[1]))
        print(convert_list_quiz)

    def __del__(self):
        del self.handler