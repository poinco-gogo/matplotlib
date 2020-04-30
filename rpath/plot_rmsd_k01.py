import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

mpl.style.use('classic')
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams["mathtext.rm"] = 'Arial'

nrep = 32
ndir = 1
ncvs = 286 * 3
ndat = 100
sref = "../eq001/output/" 
stgt = "../simanl_004_eq030_004_eq010_k01_eq010_rp" 

def load_rpath_line(fname, ar):
	for i in range(1, nrep+1):
		stmp = fname + str(i) + ".rpath"
		d = np.loadtxt(stmp)
		ar[i-1,:] = d[1:]


refs = np.zeros((nrep, ncvs))
data = np.zeros((nrep, ncvs, ndat * ndir))
load_rpath_line(sref, refs)
for i in range(1, nrep+1):
	for j in range(1, ndir+1):
		f = stgt + "{0:03d}".format(j) + "/output/" + str(i) + ".rpath"
		d = np.loadtxt(f)
		for k in range(1, ndat+1):
			l = (k-1) + ndat * (j-1)
			data[i-1, :, l] += (refs[i-1,:] - d[k-1, 1:])**2

rmsd = np.zeros((nrep, ndat*ndir))
rmsd[:,:] = np.sqrt(np.sum(data[:,:,:], axis=1)/ncvs)

for i in range(1, ndat * ndir + 1):
	dx = np.arange(1,33)
	dy = rmsd[:,i-1]
	plt.plot(dx, dy, color=cm.jet(float(i) / (ndat * ndir)))

plt.xticks([1,4,8,12,16,20,24,28,32])
plt.xlim([1, 32])
plt.xlabel("Image index",fontsize=18)
plt.ylabel("RMSD from initial image ($\AA$)",fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
sm = plt.cm.ScalarMappable(cmap=cm.jet, norm=plt.Normalize(vmin=0.1, vmax=ndat*ndir))
sm._A = []
plt.colorbar(sm)
plt.tight_layout()
plt.savefig("tmp.eps",dpi=300,transparent=True)
plt.show()
