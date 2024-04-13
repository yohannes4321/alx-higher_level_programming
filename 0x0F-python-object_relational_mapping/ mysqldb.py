#!/usr/bin/python3
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='john',
    password='1111',
    database='mydatabase'
)

mycursor = db.cursor()

# Execute SQL statement to create a table
#mycursor.execute("CREATE TABLE Person (name VARCHAR(256), age INT UNSIGNED, id INT PRIMARY KEY AUTO_INCREMENT)")

mycursor.execute("INSERT iNTO Person(name,age) values(%s,%s)",("Yohannes",19))
mycursor.execute("insert into Person(name,age) values (%s,%s)",("jhonalex",19))
db.commit()
mycursor.execute("SELECT * FROM Person")
for x in mycursor:
    print (x)