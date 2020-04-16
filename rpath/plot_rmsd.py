import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

mpl.style.use('classic')
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams["mathtext.rm"] = 'Arial'

n = 5000
for i in range(1, n+1):
	fname = str(i) + ".rmsd_k100_fp"
	d = np.loadtxt(fname)
	dx = d[:,0]
	dy = d[:,1]
	plt.plot(dx, dy, color=cm.jet(float(i) / n))

plt.xticks([1,4,8,12,16,20,24,28,32])
plt.xlim([1, 32])
plt.xlabel("Image index",fontsize=18)
plt.ylabel("RMSD from initial image ($\AA$)",fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
sm = plt.cm.ScalarMappable(cmap=cm.jet, norm=plt.Normalize(vmin=0.1, vmax=5000))
sm._A = []
plt.colorbar(sm)
plt.tight_layout()
plt.savefig("tmp.png",dpi=300)
plt.show()
