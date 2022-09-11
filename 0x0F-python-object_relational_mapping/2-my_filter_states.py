#!/usr/bin/python3
"""displays all values in the states table of \
    hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if (sys.argv) < 5:
        print("Usage: ./<script_name>.py [username]"
              "[password] [database] [state]")
        sys.exit()

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states "
                "WHERE name='{sys.argv[4]}' "
                "ORDER BY id ASC")
    the_rows = cur.fetchall()
    for (rows) in the_rows:
        print(rows)
    cur.close()
    db.close()
