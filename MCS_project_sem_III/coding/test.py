#select test_name,list of test timings(duration of test)
#[end_timing - start_timing] from test_runs, tasks
#for p60

import csv
import mysql.connector
from mysql.connector import errorcode

mydb = mysql.connector.connect(user="root",passwd="shA2189",database="rtcdb")
mycursor = mydb.cursor()

#sql = "select id,test_name from test_runs where test_name like '%p60' limit 10"
#following query will take project_id from tasks,
#test_name, started and finished time from test_runs
#where task_id from test_runs is equal to id from tasks
#and it is only applied where there is '*p60' in test_name's column

sql = "select \
(select tasks.project_id) as pro_id, \
(select test_runs.test_name) as test_name, \
(select timestampdiff(second,started,finished)) as duration \
from test_runs \
inner join tasks on test_runs.task_id=tasks.id \
where tasks.project_id like '%p60'"

#dictionary to store the names and the list of duration
dictionary = {}

try:
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for o,p,x in myresult:
		dictionary.setdefault(o, []).append(x)
			
	with open('./dictionary.csv', 'w') as csv_file:
		writer = csv.writer(csv_file)
		for key, value in dictionary.items():
			writer.writerow([key, value])
	#print(dictionary)
		
	#setdefault(o[,d])	If key is in the dictionary, return its value.
	#If not, insert key with a value of d and return d (defaults to None).
	#l.append(i)
	
except mysql.connector.Error as err:
	print("Caught something")
	print(err)

print(mycursor.rowcount,"record(s) affected")
