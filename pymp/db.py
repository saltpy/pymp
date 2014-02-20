from collections import namedtuple


__all__ = ['execute', 'map_data']

Query = namedtuple('Query', 'sql data headers')


class DbException(Exception):
    pass


def execute(conn, sql, values=None):
    cur = conn.cursor()
    try:
        if values is None:
            cur.execute(sql)
        else:
            cur.executemany(sql, values)
        data = [row for row in cur]
        try:
            headers = [i[0] for i in cur.description]
        except TypeError:
            headers = None
    except Exception as e:
        raise DbException(str(e) + "\n\t" + sql + "\n\twith values: "
                          + str(values))
    finally:
        cur.close()

    return Query(sql, data, headers)


def map_data(Type, query):
    return [Type(*data) for data in query.data]
