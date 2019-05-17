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
listListPlot=[]

fig, ax = plt.subplots()

def storeAllValuesInDict():
	for a,b in rf.iterrows():
		#if(a==60):
			#print(a)
			#break
		listList.append([])
		#testNames
		m=b[0]
		#testMean
		n= b[2]
		#listList[a].append(a)
		listList[a].append(n)
		
		listListPlot.append([])
		
		n= b[2]
		listListPlot[a].append(a)
		listListPlot[a].append(m)
		listListPlot[a].append(n)
		
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
#print("before X : \n",X)
kmeans = KMeans(n_clusters=4)
#kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
#semi-supervised learning , kmeans algorithm supplies us the labels for our data
labels = kmeans.labels_

X = listListPlot
#print("after X : \n",X)
#print("listList \n",listList)
#print("listListPlot \n",listListPlot)
print("centriod : \n",centroids)
print("centriod : \n",centroids.dtype)
#print("labels \n: ",labels)

#colors = ["g.","r."]
#colors = ["g."]
colors = ["g.","r.","y.","c."]
plt.xticks([])
for i in range(len(X)):
	#plotting x[i][0] = 0 -n ,n = number of tests
	#x[i][1] ,1 = test_names ,here plotting test_names on x axis 
	#test mean on y axis
	plt.plot(X[i][2],0,colors[labels[i]],markersize=5)

print("finished plotting")

#print("printing centroid ",centroids[:,0],centroids[:,1])
print("printing centroid ",centroids)
plt.xlabel("Test Names")
plt.ylabel("mean")
plt.scatter(centroids[:,0],[0,0,0,0],marker = "x",s = 20, linewidth = 5 , zorder = 10)
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
