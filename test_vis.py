import pandas as pd
import numpy as np
from matplotlib import pyplot as pl
from mpl_toolkits.mplot3d import Axes3D

s = np.random.randint(0,50,size=305)
u = np.random.randint(0,50,size=305)
p = np.random.randint(0,50,size=305)
lwg = np.random.sample(305)*20

fig = pl.figure()
ax = fig.add_subplot(111, projection='3d')

#for i in range(len(s)):
p=ax.scatter(s,u,p,s=lwg,c=lwg,marker='o',cmap='viridis')
ax.set_xlabel('Sulphur Intake')
ax.set_ylabel('Phosphorus Intake')
ax.set_zlabel('Urea Intake')

pl.suptitle('Liveweight Gain with Supplement Intake')

cbar = fig.colorbar(p)
cbar.set_label("Liveweight gain in kg")#, labelpad=-40)


pl.show()
