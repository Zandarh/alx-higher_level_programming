#!/usr/bin/python3
import MySQLdb
import sys
"""script that lists all states with a name starting with\
N (upper N) from the database hbtn_0e_0_usa
"""


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=data, port=3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE states.name\
                LIKE "N%" ORDER BY states.id;')
    rows = cur.fetchall()
    [print(row) for row in rows]
    cur.close()
    db.close()
    