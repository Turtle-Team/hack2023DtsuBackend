import typing

import database.handler
from database import processor
import unittest

class Test(unittest.TestCase):

    def test_take_list_group_prepods(self):
        x = database.processor.DataProcessor().get_quiz_all()
        return self.assertIsInstance(x, str)
