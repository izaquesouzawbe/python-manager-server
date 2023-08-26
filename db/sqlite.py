import sqlite3


def get_db_sqlite():
    conn = sqlite3.connect('dados.db')
    return conn


def find_one_sqlite(sql, args):
    conn = get_db_sqlite()
    cursor = conn.cursor()

    cursor.execute(sql, args)
    row = cursor.fetchone()

    cursor.close()

    return row


def find_all_sqlite(sql, args):
    conn = get_db_sqlite()
    cursor = conn.cursor()

    cursor.execute(sql, args)
    rows = cursor.fetchall()

    cursor.close()

    return rows


def execute_sql_sqlite(sql, args):
    conn = get_db_sqlite()
    cursor = conn.cursor()

    print(args)
    cursor.execute(sql, args)

    conn.commit()
    conn.close()