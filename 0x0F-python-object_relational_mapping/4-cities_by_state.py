#!/usr/bin/python3
"""
a script that list all the cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
