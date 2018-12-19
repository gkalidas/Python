#insert into table query using python

import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="shA2189",database="sakila")

mycursor = mydb.cursor()

sql = "insert into customers (name,address,id) values( %s,%s,%s)"
val = [
("Tushar","Ravet",6),
("sayali","Dange",7)
]
mycursor.executemany(sql,val)

#why mydb.commit?
#mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
mydb.commit()

print(mycursor.rowcount, "record inserted.")
