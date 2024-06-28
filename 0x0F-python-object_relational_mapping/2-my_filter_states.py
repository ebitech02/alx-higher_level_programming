#!/usr/bin/python3
"""
a script that takes in an argument and displays 
all values in the states table of hbtn_0e_0_usa where
name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """connects to the database"""
    db = MySQLdb.connnect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

     cursor = db.cursor()

     query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC".format(argv[4])

     cursor.execute(query)
     
     rows = cursor.fetchall()

     for row in rows:
         print(row)

    cursor.close()
    db.close()
