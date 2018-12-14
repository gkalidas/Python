import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="shA2189",
  database="sakila"
)

mycursor = mydb.cursor()

mycursor.execute("")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
