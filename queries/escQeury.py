import mysql.connector

mydb = mysql.connector.connect(user="root",passwd="shA2189",database="world")

mycursor = mydb.cursor()
val = ("customers",)
sql = "select * from %s"

mycursor.execute(sql,val)
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
