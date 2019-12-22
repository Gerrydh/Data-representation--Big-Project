import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="kim123",
    database="Ger",
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()
sql=""
mycursor.execute(sql)
