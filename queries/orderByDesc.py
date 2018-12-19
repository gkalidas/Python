import mysql.connector

mydb = mysql.connector.connect(user="root",passwd="shA2189",database="world")

mycursor = mydb.cursor()

sql = "select name from customers order by name desc"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
	print(x)
