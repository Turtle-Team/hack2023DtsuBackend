from unittest import TestCase


class TestDb(TestCase):
    def test_select_sub_group(self):
        import database.handler
        print(database.handler.Db().select_sub_group('TESTGROUP'))
        self.assertIs(True is True, True)
