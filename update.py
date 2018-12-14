
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="shA2189",
  database="world"
)

mycursor = mydb.cursor()
val=("parik","Parik")
sql = "update customers set lname = %s where lname = %s"
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record(s) afftected")

sql = "select * from customers"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
