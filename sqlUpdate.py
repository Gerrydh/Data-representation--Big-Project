import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="Hospital"
)

cursor = db.cursor()
sql="insert into patient (Name, Symptoms) values (%s,%s)"
values = ("Simon", "Delhi Belly")
cursor.execute(sql, values)

db.commit