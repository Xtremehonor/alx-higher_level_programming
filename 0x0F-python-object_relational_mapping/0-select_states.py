#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import MySQLdb
import sys

host = 'localhost'
user=sys.argv[1]
password=sys.argv[2]
db =sys.argv[3]


if __name__ == "__main__": 
    db = MySQLdb.connect(host=host, user=user, passwd=password, db =db[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states`")

    exists = cursor.fetchall()
    for row in exists:
        print(row)
