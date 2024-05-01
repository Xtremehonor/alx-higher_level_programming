#!/usr/bin/python3
"""
lists all cities of that state, using the database
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
    query = query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE state.name = %s
    ORDER BY cities.id ASC;
    """
    cursor.execute(query, (state,))

    exists = cursor.fetchall()
    for row in exists:
        print(row)
    cursor.close()
    db.close()
