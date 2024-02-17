#!/usr/bin/python3
""" Script that lists all states"""
import MySQLdb
import sys


if __name__ == '__main__':
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    db = MySQLdb.connect(host='localhost',
                         user=MY_USER,
                         passwd=MY_PASS,
                         db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT * from states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
