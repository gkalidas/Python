# This is from another file
import pandas as pd
rf = pd.read_csv('D:\home\git_projects\Python\MCS_project_sem_III\coding\dictionary.csv',header=None,low_memory=False)

#to slice the the series,i.e.to take only duration from the csv
rf[1]

#empty list to store the duration
list_dur=[]

for x in rf:
    #print("x",x)
    #x prints 0-number of rows in this case it is 16k...
    if(x==5):
		break;
    #stores the each row as a list, need to slice each list into list
    list_dur=rf[1].tolist()
    
print(list_dur[:3])
