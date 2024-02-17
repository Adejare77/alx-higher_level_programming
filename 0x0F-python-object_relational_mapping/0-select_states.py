#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

from sys import argv
from MySQLdb import connect

if __name__ == "__main__":
    conn = connect(user=argv[1], passwd=argv[2], db=argv[3],
                   port=3306, host="localhost", charset="utf8")

    cur = conn.cursor()
    cur.execute('SELECT id, name\
                FROM states\
                ORDER BY id ASC')
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
