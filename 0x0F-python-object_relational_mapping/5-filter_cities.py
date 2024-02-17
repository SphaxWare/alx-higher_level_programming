#!/usr/bin/python3
""" Script that lists all states"""
import MySQLdb
import sys

# The code should not be executed when imported
if __name__ == '__main__':
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    name = sys.argv[4]
    # Connect to db
    db = MySQLdb.connect(host='localhost',
                         user=MY_USER,
                         passwd=MY_PASS,
                         db=MY_DB)
    cur = db.cursor()
    query = (
            "SELECT cities.name "
            "FROM cities INNER JOIN states ON "
            "cities.state_id = states.id "
            "WHERE states.name LIKE BINARY %s"
            "ORDER BY cities.id;"
            )
    cur.execute(query, (name,))
    rows = cur.fetchall()

    for i, row in enumerate(rows):
        if i == len(rows) - 1:
            print("{}".format(row[0]), end='')
        else:
            print("{}, ".format(row[0]), end='')

    print()
    # Closing db
    db.close()
