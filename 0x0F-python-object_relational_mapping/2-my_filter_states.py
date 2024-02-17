#!/usr/bin/python3
"""Takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

from sys import argv
from MySQLdb import connect

if __name__ == '__main__':
    conn = connect(user=argv[1], passwd=argv[2], db=argv[3],
                   host="localhost", port=3306, charset="utf8")

    cur = conn.cursor()
    cur.execute('SELECT id, name\
                FROM states\
                WHERE BINARY name = "{}"\
                ORDER BY id ASC'.format(argv[4]))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
