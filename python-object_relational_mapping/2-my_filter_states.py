#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    MY_HOST = 'localhost'
    MY_USER = sys.argv[1]
    MY_PASS = ""
    MY_DB = sys.argv[3]

    db = MySQLdb.connect(host=MY_HOST, port=3306, user=MY_USER, passwd=MY_PASS, db=MY_DB)

    cur = db.cursor()

    cur.execute("""SELECT * FROM states WHERE name = '{}' ORDER
                BY id ASC;""".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
