from collections import namedtuple


class Query(namedtuple('Query', 'sql results headers')):
    def __new__(cls, sql, results=None, headers=None):
        return super(Query, cls).__new__(cls, sql, results, headers)


def execute(conn, query):
    cur = conn.cursor()
    try:
        cur.execute(query.sql)
        res = [row for row in cur]
    finally:
        cur.close()

    return Query(query.sql, res)
