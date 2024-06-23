#!/usr/bin/python3
"""
a script that lists all states from the database  hbtn_0e_0_usa
"""
import  MySQLdb
from sys import argv

if __name__ == "__main__":
    """"
    Access the database and connect to the database
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

