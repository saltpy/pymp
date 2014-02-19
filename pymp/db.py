from collections import namedtuple


__all__ = ['execute', 'map_data']


class Query(namedtuple('Query', 'sql data headers')):
    def __new__(cls, sql, data=None, headers=None):
        return super(Query, cls).__new__(cls, sql, data, headers)


def execute(conn, sql):
    cur = conn.cursor()
    try:
        cur.execute(sql)
        data = [row for row in cur]
        try:
            headers = [i[0] for i in cur.description]
        except TypeError:
            headers = None
    finally:
        cur.close()

    return Query(sql, data, headers)


def map_data(identifier, query):
    if isinstance(identifier, basestring):
        Type = namedtuple(identifier, query.headers)
    else:
        Type = identifier
    return [Type(*data) for data in query.data]
