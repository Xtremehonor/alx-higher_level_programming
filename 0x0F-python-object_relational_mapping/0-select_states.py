#!/usr/bin/python3

import MySQLdb
import sys

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

db = MySQLdb.connect(host="localhost", user=mysql_username, passwd=mysql_password, db =database_name)

try:
    cursor = db.cursor()
except MySQLdb.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))


cursor.execute("SELECT * FROM states")

exists = cursor.fetchall()

for row in exists:
    print(row)

cursor.close()
db.close()