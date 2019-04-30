***************************************************************
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
