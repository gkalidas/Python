import mysql.connector

mydb = mysql.connector.connect(user="root",passwd="shA2189",database="sakila")

mycursor = mydb.cursor()

sql = "select \
users.name as users,\
products.name as favourites \
from users \
right join products on users.fav = products.id"
mycursor.execute(sql)


myresult = mycursor.fetchall()

for x in myresult:
	print(x)
