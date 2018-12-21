import mysql.connector

mydb = mysql.connector.connect(user="root",passwd="shA2189",database="sakila")

mycursor = mydb.cursor()

sql = "update users set fav = %s where fav = %s"
val = [
(154,134),
(155,135),
(156,136)
]
mycursor.executemany(sql,val)
mydb.commit()

print(mycursor.rowcount,"record(s) affected")
