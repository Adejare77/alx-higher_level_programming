#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""

from sys import argv
from MySQLdb import connect

if __name__ == '__main__':
    conn = connect(user=argv[1], passwd=argv[2], db=argv[3],
                   port=3306, host="localhost", charset="utf8")

    cur = conn.cursor()
    cur.execute('SELECT cities.name\
                FROM cities\
                JOIN states ON states.id = cities.state_id\
                WHERE BINARY states.name LIKE BINARY %s\
                ORDER BY cities.id ASC', (argv[4].encode(),))

    rows = cur.fetchall()
    rows_list = [row[0] for row in rows]
    print(*rows_list, sep=", ")
