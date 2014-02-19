import unittest

import sqlite3

from db import Query, execute


class TestDb(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.create_sql = """CREATE TABLE people
                                (id INTEGER PRIMARY_KEY,
                                 name TEXT,
                                 email TEXT,
                                 level INTEGER,
                                 manager INTEGER)"""
        self.insert_manager = """INSERT INTO people VALUES
                                    (1,
                                    "Mick Manager",
                                     "mick.manager@test.com",
                                     4,
                                     1)"""
        self.insert_tester = """INSERT INTO people VALUES
                                    (2,
                                    "Toby Tester",
                                     "toby.tester@test.com",
                                     3,
                                     1)"""
        self.select_all = """SELECT * FROM people"""

    def tearDown(self):
        self.conn.close()

    def test_execution_causes_db_to_change(self):
        execute(self.conn, Query(self.create_sql, None))
        execute(self.conn, Query(self.insert_manager, None))
        execute(self.conn, Query(self.insert_tester, None))
        expected = [(1, u'Mick Manager', u'mick.manager@test.com', 4, 1),
                    (2, u'Toby Tester', u'toby.tester@test.com', 3, 1)]

        actual = execute(self.conn, Query(self.select_all, None)).results

        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
