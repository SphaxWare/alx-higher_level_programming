#!/usr/bin/python3
import MySQLdb
import sys
"""
 lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""
def main():
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    db = MySQLdb.connect(host='localhost', user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT * from states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
