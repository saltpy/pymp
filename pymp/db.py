from collections import namedtuple


class Query(namedtuple('Query', 'sql results headers')):
    def __new__(cls, sql, results=None, headers=None):
        return super(Query, cls).__new__(cls, sql, results, headers)


def execute(conn, query):
    cur = conn.cursor()
    try:
        cur.execute(query.sql)
        res = [row for row in cur]
        try:
            headers = [i[0] for i in cur.description]
        except TypeError:
            headers = None
    finally:
        cur.close()

    return Query(query.sql, res, headers)


def map_results(name, query):
    Typ = namedtuple(name, query.headers)
    return [Typ(*res) for res in query.results]
