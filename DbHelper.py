from pymysql import *

def get_all_data(query, parameters=None):
    conn = connect(host='localhost', database='practice_admin', user='root', password='root')
    cur = conn.cursor()
    if (parameters is None):
        cur.execute(query)
    else:
        cur.execute(query % parameters)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def get_data(query, parameters=None):
    conn = connect(host='localhost', database='practice_admin', user='root', password='root')
    cur = conn.cursor()
    if (parameters is None):
        cur.execute(query)
    else:
        cur.execute(query % parameters)
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result


def execute_query(query, parameters=None):
    conn = connect(host='localhost', database='practice_admin', user='root', password='root')
    cur = conn.cursor()
    if (parameters is None):
        cur.execute(query)
    else:
        cur.execute(query % parameters)
    conn.commit()
    cur.close()
    conn.close()

