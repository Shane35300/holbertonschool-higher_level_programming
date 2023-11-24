#!/usr/bin/python3
"""
This script connects to a MySQL server and retrieves
rows from the 'states' table based on a given condition.
"""


import MySQLdb
import sys

"""
    This script connects to a MySQL server and
    retrieves rows from the 'states' table based on a given condition.

    Usage: ./script.py <username> <password> <database> <state_name>

    Args:
        - <username>: MySQL username
        - <password>: MySQL password
        - <database>: MySQL database name
        - <state_name>: Name of the state to search for in the 'states' table

    Example:
        ./script.py root root hbtn_0e_0_usa California
"""


if __name__ == "__main__":
    """
    Args:
        - <username>: MySQL username
        - <password>: MySQL password
        - <database>: MySQL database name
        - <state_name>: Name of the state to search for in the 'states' table
    """
    if len(sys.argv) != 5:
        sys.exit(1)

    MY_HOST = 'localhost'
    MY_USER = sys.argv[1]
    MY_PASS = ""
    MY_DB = sys.argv[3]

    db = MySQLdb.connect(
        host=MY_HOST,
        port=3306,
        user=MY_USER,
        passwd=MY_PASS,
        db=MY_DB
    )

    cur = db.cursor()
    state_name = sys.argv[4]
    cur.execute("""SELECT * FROM states WHERE name = %s ORDER
                BY id ASC;""", (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
