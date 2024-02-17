#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

from sys import argv
from MySQLdb import connect

if __name__ == '__main__':
    conn = connect(user=argv[1], passwd=argv[2], db=argv[3],
                   host="localhost", charset="utf8", port=3306)

    cur = conn.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name\
                FROM states\
                JOIN cities ON cities.state_id = states.id\
                ORDER BY cities.id')
    rows = cur.fetchall()
    for row in rows:
        print(row)
