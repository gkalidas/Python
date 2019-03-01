***************************************************************
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from pandas import DataFrame
import re
pwd = 
engine = create_engine('mysql+mysqlconnector://root:',pwd,'@localhost/rtcdb')
sql = "select \
(select tasks.project_id) as pro_id, \
(select test_runs.test_name) as test_name, \
(select timestampdiff(second,started,finished)) as duration \
from test_runs \
inner join tasks on test_runs.task_id=tasks.id \
where tasks.project_id like '%p60' limit 10"

data = pd.read_sql_query(sql, engine)

print(data.iloc[0])

dataDict = {}
for i,r in data.iterrows():
    #print(data['test_name'].iloc[i],data['test_name'].iloc[1])
    dataDict.setdefault(data['test_name'].iloc[i],[]).append(data['duration'].iloc[i])
    
writeDataDict={}
pd.DataFrame(writeDataDict).T.reset_index().to_csv('D:\home\git_projects\Python\MCS_project_sem_III\coding\dictTestNames.csv', header=False, index=False)
with open('D:\home\git_projects\Python\MCS_project_sem_III\coding\dictTestNames.csv', 'a',encoding='utf') as f:
    for x,y in dataDict.items():
        writeDataDict.setdefault(x,y)
        #df = pd.DataFrame(data)
        df = pd.DataFrame.from_dict(writeDataDict, orient='index')
        df.to_csv(f,header=False)
        writeDataDict={}
        
count=0
prev_count=0
for x,y in dataDict.items():
    prev_count =len(y)
    if(prev_count>=count):
        count=prev_count
        z=x
    if(x=="asm_bas_active_comp_insert_here_esr_p60"):
        print(x)

print(z,count)

###############################################################

import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from pandas import DataFrame
import re

engine = create_engine('mysql+mysqlconnector://root:shA2189@localhost/rtcdb')
sql = "select \
(select tasks.project_id) as pro_id, \
(select test_runs.test_name) as test_name, \
(select timestampdiff(second,started,finished)) as duration \
from test_runs \
inner join tasks on test_runs.task_id=tasks.id \
where tasks.project_id like '%p60'"

data = pd.read_sql_query(sql, engine)
print(data)
dictionary = {}
for x,y in data.iterrows():
    #print(x,y)
    dictionary.setdefault(y[0], []).append(y[2])
#print(dictinary)

dataDict={}
pd.DataFrame(dataDict).T.reset_index().to_csv('D:\home\git_projects\Python\MCS_project_sem_III\coding\dictFromPandas.csv', header=False, index=False)
with open('D:\home\git_projects\Python\MCS_project_sem_III\coding\dictFromPandas.csv', 'a',encoding='utf') as f:
    for x,y in dictionary.items():
        dataDict.setdefault(x,y)
        #df = pd.DataFrame(data)
        df = pd.DataFrame.from_dict(dataDict, orient='index')
        df.to_csv(f,header=False)
        dataDict={}
        
rf = pd.read_csv('D:\home\git_projects\Python\MCS_project_sem_III\coding\dictionary.csv',header=None,low_memory=False)

for x,y in rf.iterrows():
    if(x==0):
        print(y[0],y[1])
    if(x==2):
        y[1]= re.sub('[] ', '',y[1])
        print(y[0],y[1])
        break
 
