import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('classic')
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams["mathtext.rm"] = 'Arial'

data1=np.loadtxt('fene1.dat', comments="REMARK")
x=data1[:,0]

y1=data1[:,1]

piv=9999
for i in range(0, 32):
	if y1[i] < piv:
		piv = y1[i]

for i in range(0, 32):
	y1[i] -= piv

data2=np.loadtxt('fene1_block10_error.dat')
y2=data2[:,1]

#plt.plot(x,y1,color='m',alpha=0.6,lw=2, marker='o')
#plt.plot(x,y1,color='#1f77b4',alpha=0.6,lw=2, marker='o')
plt.figure(figsize=(4,3))
#plt.plot(x,y1,color='#1f77b4',lw=2, marker='o')
plt.errorbar(x, y1, yerr=y2, color='#1f77b4',lw=2, marker='o')
#plt.errorbar(x,y1,yerr=err)
plt.xlabel("Image index",fontsize=18)
plt.ylabel("Free energy (kcal/mol)",fontsize=18)
plt.ylim([-0.1,4.5])
plt.xlim([0,33])
#plt.ylim([0,30])
plt.xticks([1,4,8,12,16,20,24,28,32])
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.grid()
plt.tight_layout()
plt.savefig("tmp.png",dpi=300)
plt.show()
