import unittest

import sqlite3

from db import execute, map_data
from _test_utils import (
    Person, PRAGMA_FOREIGN_KEYS, CREATE_PEOPLE_TABLE, CREATE_LEVELS_TABLE,
    INSERT_PEOPLE, INSERT_LEVELS, LEVEL_DATA, PEOPLE_DATA, SELECT_TESTER)


class TestDb(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(':memory:')

        self.shallow_tester = Person(2, u"Toby Tester",
                                     u"toby.tester@test.com", 3, 1)

        execute(self.conn, PRAGMA_FOREIGN_KEYS)
        execute(self.conn, CREATE_LEVELS_TABLE)
        execute(self.conn, CREATE_PEOPLE_TABLE)
        execute(self.conn, INSERT_LEVELS, values=LEVEL_DATA)
        execute(self.conn, INSERT_PEOPLE, values=PEOPLE_DATA)

    def tearDown(self):
        self.conn.close()

    def test_map_data(self):
        tester = map_data(Person, execute(self.conn, SELECT_TESTER))[0]

        self.assertEquals(self.shallow_tester, tester)


if __name__ == '__main__':
    unittest.main()
