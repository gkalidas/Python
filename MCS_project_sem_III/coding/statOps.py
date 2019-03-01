import pandas as pd
import numpy as np
a=122377
rf = pd.read_csv('D:\home\git_projects\Python\MCS_project_sem_III\coding\dictTestNames.csv',header=None,low_memory=False,names=range(a))
dictFP = {}

for x,y in rf.iterrows():
    count=0
    for n in y:
        if(count==0):
            dictFP[y[0]] =[]
            count+=1
        else:
            dictFP.setdefault(y[0], []).append(n)
        

#dictMD contains key and list as values
dictMD={}

for key, value in dictFP.items():
	listMD=[]
    lengthOfList= len(value) - np.count_nonzero(np.isnan(value))
    listMD.append(lengthOfList)
    meanOfList=np.nanmean(value)
    listMD.append(meanOfList)
    minFromList = np.nanmin(value)
    listMD.append(minFromList)
    maxFromList = np.nanmax(value)    
    listMD.append(maxFromList)
    stdFromList = np.nanstd(value)
    listMD.append(stdFromList)
    medianOfList = np.nanmedian(value)
    listMD.append(medianOfList)
    
    dictMD.setdefault(key,listMD)
    print(key)

dataDict={}
pd.DataFrame(dataDict).T.reset_index().to_csv('D:\home\git_projects\Python\MCS_project_sem_III\coding\dictStatOps.csv', header=False, index=False)
with open('D:\home\git_projects\Python\MCS_project_sem_III\coding\dictStatOps.csv', 'a',encoding='utf') as f:
    for x,y in dictMD.items():
        dataDict.setdefault(x,y)
        #df = pd.DataFrame(data)
        df = pd.DataFrame.from_dict(dataDict, orient='index')
        df.to_csv(f,header=False)
        dataDict={}	


