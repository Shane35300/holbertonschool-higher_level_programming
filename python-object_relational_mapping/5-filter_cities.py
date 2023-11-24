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
    cur.execute("""SELECT cities.name
                FROM cities
                JOIN states ON states.id = cities.state_id
                WHERE states.name = %s
                ORDER BY cities.id ASC;""", (sys.argv[4],))
    rows = cur.fetchall()
    trap = 0
    for row in rows:
        if trap == 1:
            print(", ", end="")
        print(row[0], end="")
        trap = 1
    print()

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
