import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.linear_model import LinearRegression
#from sklear.family import model
import pandas as pd
from sklearn.cluster import KMeans

rf = pd.read_csv('D:\home\git_projects\Python\MCS_project_sem_III\coding\\stasOpsNormTestData.csv',low_memory=False)

dictAllValues={}
listList=[]

fig, ax = plt.subplots()

def storeAllValuesInDict():
	for a,b in rf.iterrows():
		if(a==40):
			break
		listList.append([])
		n= b[2]
		listList[a].append(a)
		listList[a].append(n)
		
		count = 0
		for v in b:
			if(count==0):
				dictAllValues.setdefault(a,[v])
				count+=1
			else:
				dictAllValues.setdefault(a,[]).append(v)

storeAllValuesInDict()
#for key,values in dictAllValues.items():
#	print(key,values)
print("stored all values in dictAllValues")

#xticks will disable the names of the tests
#plt.xticks([])
#scatter() plot the graph
#sc = plt.scatter(x,y)
#plt.show()
X = listList
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
#semi-supervised learning , kmeans algorithm supplies us the labels for our data
labels = kmeans.labels_

#print("listList",listList)

print("centriod : ",centroids)
#print("labels : ",labels)

colors = ["g.","r.","y.","c."]

for i in range(len(X)):
	plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=5)

print("finished plotting")
plt.scatter(centroids[:,0],centroids[:,1],marker = "x",s = 20, linewidth = 5 , zorder = 10) 
annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def getAllValuesFromDictionary(keyName):
	for key,value in dictAllValues.items():
		if(key==keyName):
			keyValues=value
	return keyValues

def update_annot(ind):

    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    #print("position",pos)
    testName = pos[0]
    xvalue= getAllValuesFromDictionary(testName)
    text = "test name = {} \nlength = {}\nmean = {}\nminValue = {} \n\
maxValue = {} \nstdDev = {} \nmedian = {}\
".format(xvalue[0],xvalue[1],xvalue[2],xvalue[3],xvalue[4],xvalue[5],xvalue[6])
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.4)

def hover(event):
	#initialy FALSE
    vis = annot.get_visible()

   #This is the mouse location in data coords.
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        #example - True {'ind': array([11], dtype=int32)}
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

#fig.canvas.mpl_connect("motion_notify_event", hover)
plt.show()
