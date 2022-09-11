#!/usr/bin/python3

""""script that lists all states from the database hbtn_0e_0_usa:
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: ./<script_name>.py [username] [password] [database]")
        sys.exit()

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    the_rows = cur.fetchall()
    for rows in the_rows:
        print(rows)
    cur.close()
    db.close()
