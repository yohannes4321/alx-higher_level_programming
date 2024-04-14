#!/usr/bin/python3
import MySQLdb
import sys 

if __name__ == "__main__":
    args = sys.argv
    username = args[1]
    password = args[2]
    database = args[3]
    
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
    