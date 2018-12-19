import mysql.connector

mydb = mysql.connector.connect(user="root",passwd="shA2189",database="sakila")

mycursor = mydb.cursor()

sql = "update customers set address = %s where address = %s"
val = ("kothrud","ravet")
mycursor.execute(sql,val)
mydb.commit()

print(mycursor.rowcount,"record(s) affected")
