#!/usr/bin/python3
from datetime import datetime
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='john',
    password='1111',
    database='mysqldb2'
)

mycursor = db.cursor()

# Add a new column to the existing table
#mycursor.execute("ALTER TABLE Student drop food")
#mycursor.execute('ALTER TABLE Student CHANGE  name firstname VARCHAR(23)')
# Committing the transaction
#db.commit()
mycursor.execute('DESCRIBE Student')
for my in mycursor:
    print(my)