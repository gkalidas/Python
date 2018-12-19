import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shA2189",
  database="sakila"
)

mycursor = mydb.cursor()
query = "alter table customers add column id int primary key"
mycursor.execute(query)

for x in mycursor:
	print (x)
