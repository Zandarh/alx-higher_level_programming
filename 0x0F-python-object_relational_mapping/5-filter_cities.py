#!/usr/bin/python3
"""displays all values in the  city table of \
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
    cur.execute("SELECT b.name "
                "FROM states a "
                "LEFT JOIN cities b "
                "ON a.id = b.state_id "
                "WHERE a.name = %s "
                "ORDER BY b.id ASC",
                (sys.argv[4], ))
    the_rows = cur.fetchall()
    query_len = len(the_rows)
    for i in range(the_rows):
        if i < query_len - 1:
            print(the_rows[i][0], end=', ')
        else:
            print(the_rows[i][0])
    cur.close()
    db.close()
