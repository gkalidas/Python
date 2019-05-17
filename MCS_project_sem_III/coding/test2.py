import numpy as np
import matplotlib.pyplot as plt
 
# Create data
N = 60
g1 = (0.6  * np.random.rand(N), 0.2 * np.random.rand(N))
g2 = (0.6 * np.random.rand(N), 0.4*np.random.rand(N))
g3 = (0.6*np.random.rand(N),0.6*np.random.rand(N))
g4 = (0.6 *np.random.rand(N),0.8*np.random.rand(N))

data = (g1, g2,g3,g4)
colors = ("red", "green", "blue","gray")
groups = ("coffee", "tea", "water","mati")

print("printing g1 :",g1)
# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
count = 0
for data, color, group in zip(data, colors, groups):
	x, y = data
	count+=1
	ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
 
plt.title('Matplot scatter plot')
print("count is " ,count)
plt.legend(loc=2)
plt.show()
