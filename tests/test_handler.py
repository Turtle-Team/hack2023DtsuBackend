import typing
from unittest import TestCase


class TestDb(TestCase):
    def test_select_quiz_all(self):
        import database.handler
        all_quiz = database.handler.Db().select_quiz_all()
        self.assertIs(type(all_quiz), list)

    def test_select_answer_all(self):
        import database.handler
        all_quiz = database.handler.Db().select_answer_all()
        self.assertIs(type(all_quiz), list)

