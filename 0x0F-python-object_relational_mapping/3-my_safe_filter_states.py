#!/usr/bin/python3
"""
displays all values in the 'states' from database hbtn_0e_0_usa.
Usage: ./0-select_states.py <user> <passwd> <db> <state>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    state = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cursor.execute(query, (state,))

    exists = cursor.fetchall()
    for row in exists:
        print(row)
    cursor.close()
    db.close()
