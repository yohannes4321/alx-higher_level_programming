#!/usr/bin/python3
"""Script to connect to MySQL database and retrieve states from the 'states' table."""

import MySQLdb
import sys

def main():
    """Main function to execute the script."""
    args = sys.argv[1:]
    if len(args) != 3:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = args

    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
    except MySQLdb.Error as e:
        print("MySQL connection error:", e)
        sys.exit(1)

    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        results = cursor.fetchall()

        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL query error:", e)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
