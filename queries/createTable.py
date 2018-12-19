import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shA2189",
  database="sakila"
)

mycursor = mydb.cursor()
query = "create table a(name varchar(220) primary key,address varchar(220))"
mycursor.execute(query)

for x in mycursor:
	print (x)
