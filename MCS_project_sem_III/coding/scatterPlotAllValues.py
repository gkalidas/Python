import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
import pandas as pd

rf = pd.read_csv('D:\home\git_projects\Python\MCS_project_sem_III\coding\\stasOpsNormTestData.csv',low_memory=False)

test_names=[]
test_mean=[]
dictAllValues={}

def storeAllValuesInDict():
	for a,b in rf.iterrows():
		if(a==6):
			break
		test_names.append(b[0])
		test_mean.append(b[2])
		count = 0
		for v in b:
			if(count==0):
				dictAllValues[b[0]]=[]
				count+=1
			else:
				dictAllValues.setdefault(b[0],[]).append(v)

def getAllValuesFromDictionary(keyName):
	for key,value in dictAllValues.items():
		if(key==keyName):
			keyValues=value
	return keyValues

storeAllValuesInDict()
print("stored all values in dictAllValues")
x=test_names
y=test_mean

fig, ax = plt.subplots()

#x and y axix labels
plt.xlabel("test names")
plt.ylabel("mean")

#ticks([]) will hide the values on x and y axis respectively
plt.xticks([])

plt.title('Normal Test Data')

#scatter() plot the graph
sc = plt.scatter(x,y)

annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):

    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    testName = x[int(pos[0])]
    xvalue= getAllValuesFromDictionary(testName)
    text = "test name = {} \nlength = {}\nmean = {}\nminValue = {} \n\
maxValue = {} \nstdDev = {} \nmedian = {}\
".format(testName,xvalue[0],xvalue[1],xvalue[2],xvalue[3],xvalue[4],xvalue[5])
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

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()
