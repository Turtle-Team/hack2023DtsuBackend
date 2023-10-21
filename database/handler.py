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

#это определенные квизы, но он выдает сразу все в виде кортежей
    def select_quiz(self, quiz_name):
        try:
            query = "SELECT * FROM quiz WHERE name = %s"
            self.cursor.execute(query, (quiz_name,))  # передаем имя квиза как параметр

            result = self.cursor.fetchall()

            return result
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return None

    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


