from scipy.interpolate import griddata
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show,pcolor
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as ml

x = np.loadtxt("xi.mat")
y = np.loadtxt("yi.mat")
z = np.loadtxt("pmf.mat")

X, Y = meshgrid(x, y)

interval1 = np.arange(0, 6, 0.4)

fig, ax1 = plt.subplots(nrows=1)

ax1.contour(X, Y, z, interval1,linewidths=0.5, colors='k')

cntr1 = ax1.contourf(X, Y, z, interval1,cmap="GnBu_r")

cbar = plt.colorbar(cntr1)
cbar.set_label("PMF (kcal/mol)")
plt.xlim([-180,20])
plt.ylim([ -70,180])
plt.xlabel("Phi (degree)")
plt.ylabel("Psi (degree)")
plt.savefig("tmp.png", dpi=300)
plt.show()
