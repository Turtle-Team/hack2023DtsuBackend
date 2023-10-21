import typing

import database.handler
from database import processor
import unittest

class Test(unittest.TestCase):

    def test_get_all_quiz(self):
        x = database.processor.DataProcessor().get_all_quiz()
        print(x)
        return self.assertIsInstance(x, str)
