
import mysql.connector

mydb = mysql.connector.connect(user="root",passwd="shA2189",database="world")

mycursor = mydb.cursor()

sql = "delete from customers where name = %s"
val = ("Vaibhav",)
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount,"record(s) deleted")
