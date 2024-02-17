#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
from MySQLdb import connect
from sys import argv

if __name__ == '__main__':
    conn = connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306,
                   charset="utf8", host="localhost")
    cur = conn.cursor()

    cur.execute('SELECT id, name\
                FROM states\
                WHERE name LIKE BINARY "N%"\
                ORDER BY id ASC')

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
