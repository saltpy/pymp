import unittest

import sqlite3

from db import Query, execute, map_data


class Person(object):
    def __init__(self, id, name, email, level, manager):
        self.id = id
        self.name = name
        self.email = email
        self.level = level
        self.manager = manager


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
        self.select_manager_by_id = """SELECT *
                                       FROM people
                                       WHERE people.id == 1"""

        self.manager = (1, u'Mick Manager', u'mick.manager@test.com', 4, 1)
        self.tester = (2, u'Toby Tester', u'toby.tester@test.com', 3, 1)

    def tearDown(self):
        self.conn.close()

    def _make_people_table(self):
        execute(self.conn, Query(self.create_sql))
        execute(self.conn, Query(self.insert_manager))
        execute(self.conn, Query(self.insert_tester))

    def test_execution_causes_db_to_change(self):
        self._make_people_table()
        expected = [self.manager, self.tester]

        actual = execute(self.conn, Query(self.select_all)).data

        self.assertEquals(expected, actual)

    def test_a_query_should_record_the_headers_for_its_cursor(self):
        self._make_people_table()
        expected = ['id', 'name', 'email', 'level', 'manager']

        actual = execute(self.conn, Query(self.select_all)).headers

        self.assertEquals(expected, actual)

    def test_can_get_data_as_objects(self):
        self._make_people_table()

        manager = map_data("Person",
                           execute(self.conn,
                                   Query(self.select_manager_by_id)))[0]

        self.assertEquals(self.manager[0], manager.id)
        self.assertEquals(self.manager[1], manager.name)
        self.assertEquals(self.manager[2], manager.email)
        self.assertEquals(self.manager[3], manager.level)
        self.assertEquals(self.manager[4], manager.manager)

    def test_can_map_with_custom_object(self):
        self._make_people_table()

        manager = map_data(Person,
                           execute(self.conn,
                                   Query(self.select_manager_by_id)))[0]

        self.assertEquals(self.manager[0], manager.id)
        self.assertEquals(self.manager[1], manager.name)
        self.assertEquals(self.manager[2], manager.email)
        self.assertEquals(self.manager[3], manager.level)
        self.assertEquals(self.manager[4], manager.manager)


if __name__ == '__main__':
    unittest.main()
