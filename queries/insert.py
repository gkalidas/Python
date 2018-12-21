#insert into table query using python

import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="shA2189",database="sakila")

mycursor = mydb.cursor()

sql = "insert into products (id,name) values( %s,%s)"
val = [
(1,"John"),
(2,"Peter"),
(3,"Amy")
]
mycursor.executemany(sql,val)

#why mydb.commit?
#mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
mydb.commit()

print(mycursor.rowcount, "record inserted.")
