from scipy.interpolate import griddata
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show,pcolor
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as ml

x = np.loadtxt("../pmf/xi.mat")
y = np.loadtxt("../pmf/yi.mat")
z = np.loadtxt("../pmf/pmf.mat")
X, Y = meshgrid(x, y)
interval = np.arange(0, 6, 0.2)
#plt.contourf(X, Y, z,interval,cmap=cm.GnBu)
#c1 = plt.contourf(X, Y, z,interval,cmap=cm.RdBu_r)
c1 = plt.contourf(X, Y, z,interval,cmap=cm.jet)
#c1 = plt.contourf(X, Y, z,interval,cmap=cm.gist_earth)
c2 = plt.contour(c1,interval,colors='k',alpha=0.6,linewidths=0.5)

#for i in range(2, 50):
#	if (i % 10 != 1):
#		continue;
#	fname = str(i) + ".dat"
#	d = np.loadtxt(fname)
#	dx = d[:,1]
#	dy = d[:,2]
#	plt.plot(dx, dy, color='y',marker='o', lw=0.5, ms=3.0)

#for i in range(50, 51):
#	if (i % 10 != 1):
#		continue;
#	fname = str(i) + ".dat"
#	d = np.loadtxt(fname)
#	dx = d[:,1]
#	dy = d[:,2]
#	plt.plot(dx, dy, color='k',marker='o', lw=1.5, ms=4.5)

for i in range(1, 2):
#	if (i % 10 != 1):
#		continue;
	fname = str(i) + ".dat"
	d = np.loadtxt(fname)
	dx = d[:,1]
	dy = d[:,2]
	plt.plot(dx, dy, color='r',marker='o', lw=1.5, ms=4.5)

cbar = plt.colorbar(c1)
cbar.set_label("PMF (kcal/mol)")
plt.xlim([-180,20])
plt.ylim([ -70,180])
plt.xlabel("Phi (degree)")
plt.ylabel("Psi (degree)")
plt.savefig("tmp.png", dpi=300)
plt.show()

#print(z.shape)

#xi = np.linspace(-180.0, 180.0, 180)
#yi = np.linspace(-180.0, 180.0, 180)

#Z = griddata((x, y), z, (xi, yi), method='nearest')

#plt.contourf(xi, yi, Z)
#plt.show()

#data = np.loadtxt("out")


#print(data.shape)
#print(data[179])
#print(data[180])
#print(data[181])
#print(type(data))
#x = data[:,0]
#y = data[0,:]

#print(x)
