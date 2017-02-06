import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

import mpl_toolkits.mplot3d

x,y=np.mgrid[0:20:20j,0:20:20j]
# z=x*np.exp(-x**2-y**2)
z = 2*x*x + 12*x*y + 7*y*y

ax=plt.subplot(111,projection='3d')
ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()