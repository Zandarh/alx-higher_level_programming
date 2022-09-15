#!/usr/bin/python3
"""Acts like 2-filter but safe from MySQL injections
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
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
