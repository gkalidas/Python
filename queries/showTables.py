import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="shA2189",database="sakila")

mycursor = mydb.cursor()

sql = "show tables"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
