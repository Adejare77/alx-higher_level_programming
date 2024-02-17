#!/usr/bin/python3
"""SQL Injection"""

from sys import argv
from MySQLdb import connect

if __name__ == '__main__':
    conn = connect(user=argv[1], passwd=argv[2], db=argv[3],
                   host="localhost", port=3306, charset="utf8")

    cur = conn.cursor()
    cur.execute('SELECT id, name\
                FROM states\
                WHERE BINARY name LIKE BINARY %s\
                ORDER BY id ASC', (argv[4].encode(),))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
