import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="shA2189",
  database="sakila"
)

print(mydb)
