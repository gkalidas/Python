import mysql.connector

mycursor = mysql.connector.connect(user="root",passwd="shA2189",database="sakila")

mydb = mycursor.cursor()

sql = "drop table if exists a"

mydb.execute(sql)
