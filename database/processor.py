import json
import typing

import database.handler
import database.obj

from swagger.quiz.route import Questions

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

    class DbExecution:
        def __init__(self, questions):
            self.Questions = Questions

        def get_quiz_data(self):
            data = []
            current_quiz = None

            results = self.Questions.questions()

            for row in results:
                quiz_id, quiz_name, answer_id, answer_name, is_answer = row

                if not current_quiz or current_quiz['quiz_id'] != quiz_id:
                    if current_quiz:
                        data.append(current_quiz)
                    current_quiz = {'quiz_id': quiz_id, 'quiz_name': quiz_name, 'answers': []}

                current_quiz['answers'].append({
                    'answer_id': answer_id,
                    'answer_name': answer_name,
                    'is_answer': bool(is_answer)
                })

            if current_quiz:
                data.append(current_quiz)

            return json.dumps(data, ensure_ascii=False)

    def __del__(self):
        del self.Questions