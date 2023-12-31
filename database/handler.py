import datetime
import hashlib
import random
import typing

import mysql.connector

import database.processor
import settings


class Db:
    """Вызывается через with as, берет расписание с sqlite файла shcedule.sql"""

    def __init__(self):
        self.connection = mysql.connector.connect(user=settings.DATABASE['login'],
                                                  host=settings.DATABASE['ip'],
                                                  database=settings.DATABASE['basename'],
                                                  password=settings.DATABASE['password'])
        self.cursor = self.connection.cursor()

    def select_quiz_completion(self, username: str, quiz_id: bool) -> bool:
        query = "SELECT is_complete FROM users WHERE login = %s AND quiz_to = %s"
        self.cursor.execute(query, (username, quiz_id))

        result = self.cursor.fetchone()

        if result and result[0]:
            return True
        else:
            return False


    def select_quiz_by_id(self, quiz_id: int) -> typing.List[typing.Any]:
        query = "SELECT * FROM quiz WHERE quiz_id = %s"
        self.cursor.execute(query, (quiz_id,))  # передаем имя квиза как параметр
        result = self.cursor.fetchall()
        return result

    def select_quiz_by_id(self, quiz_id: int) -> typing.List[typing.Any]:
        query = "SELECT * FROM quiz WHERE quiz_id = %s"
        self.cursor.execute(query, (quiz_id,))  # передаем имя квиза как параметр
        result = self.cursor.fetchall()
        return result

    def select_quiz_all(self) -> typing.List[typing.Any]:
        query = "SELECT * FROM quiz"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def select_answer_all(self) -> typing.List[typing.Any]:
        query = "SELECT * FROM answer"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def select_answer_by_quiz_id(self, quiz_id: int) -> typing.List[typing.Any]:
        query = "SELECT * FROM answer WHERE id_quiz = %s"
        self.cursor.execute(query, (quiz_id,))
        result = self.cursor.fetchall()
        return result

    def insert_new_answer(self, login: int, quiz_id: int):
        query = "INSERT INTO `user_answer`(`login`, `quiz_to`, `is_complete`) VALUES (%s,%s,%s)"
        self.cursor.execute(query, (login, quiz_id, True))
        result = self.cursor.fetchall()
        return result

    def select_user_answer(self, user: str):
        query = "SELECT * FROM `user_answer` WHERE login = %s   "
        self.cursor.execute(query, (user, ))
        result = self.cursor.fetchall()
        return result

    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


