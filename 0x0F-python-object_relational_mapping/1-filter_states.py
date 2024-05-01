#!/usr/bin/python3
"""
Lists all states starting with "N" from database hbtn_0e_0_usa.
Usage: ./0-select_states.py <user> <passwd> <db>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    exists = cursor.fetchall()
    for row in exists:
        print(row)
    cursor.close()
    db.close()
