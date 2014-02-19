from collections import namedtuple


Query = namedtuple('Query', 'sql results')


def execute(conn, query):
    cur = conn.cursor()
    res = []
    try:
        cur.execute(query.sql)
        res = [row for row in cur]
    finally:
        cur.close()

    return Query(query.sql, res)
