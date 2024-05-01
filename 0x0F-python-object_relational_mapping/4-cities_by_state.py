#!/usr/bin/python3
"""
displays all values in the 'states' from database hbtn_0e_0_usa.
Usage: ./0-select_states.py <user> <passwd> <db> <state>
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
    query = query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cursor.execute(query)

    exists = cursor.fetchall()
    for row in exists:
        print(row)
    cursor.close()
    db.close()
