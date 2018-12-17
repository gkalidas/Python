import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="shA2189",
  database="sakila"
)

mycursor = mydb.cursor()
query = "show databases"
mycursor.execute(query)

for x in mycursor:
	print (x)
