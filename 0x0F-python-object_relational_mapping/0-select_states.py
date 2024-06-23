#!/usr/bin/python3
"""
a script that lists all states from the database  hbtn_0e_0_usa
"""
import  MySQLdb
import sys

if __name__ == "__main__":
    """
    retrieve the MySQL username, password and database from the command line arguments
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    """
    Access the database and connect to the database
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

