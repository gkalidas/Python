import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
import pandas as pd

rf = pd.read_csv('D:\home\git_projects\Python\MCS_project_sem_III\coding\dictStatOps.csv',low_memory=False,usecols=[0,2])

test_names=[]
test_mean=[]
for a,b in rf.iterrows():
	test_names.append(b[0])
	test_mean.append(b[1])

x=test_names
y=test_mean

fig, ax = plt.subplots()

#x and y axix labels
plt.xlabel("test names")
plt.ylabel("mean")

#ticks([]) will hide the values on x and y axis respectively
plt.xticks([])

#scatter() plot the graph
sc = plt.scatter(x,y)


annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):

    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "{}".format(x[int(pos[0])])
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
