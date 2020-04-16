import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('classic')
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams["mathtext.rm"] = 'Arial'

fig, ax = plt.subplots(nrows=8, ncols=4, figsize=(12,24),sharex=True, sharey=True)

def plot_restrnt_energy(aa, irep):
	fname = "../eq001/output/" + str(irep) + ".log"
	d  = np.loadtxt(fname, skiprows=2, usecols=(1,4))
	x = d[:,0]
	y = d[:,1]
	for ii in range(2, 11):
		fname = "../eq" + "{0:03d}".format(ii) + "/output/" + str(irep) + ".log"
		d  = np.loadtxt(fname, skiprows=2, usecols=(1,4))
		dt = 400000 * (ii - 1)
		x = np.concatenate((x, d[:,0] + dt), axis=0)
		y = np.concatenate((y, d[:,1]), axis=0)
	x = x / 400000.0
	b=np.ones(15)/15.0
	aa.plot(x, y, 'r', label=irep)
	aa.legend()
	aa.grid(which='both',linestyle='--',linewidth=0.5)

for i in range(0, 8):
	for j in range(0, 4):
		plot_restrnt_energy(ax[i][j], 4 * i + j + 1)

#plt.legend(loc="best")
plt.tight_layout
plt.savefig("tmp.png", dpi=300, transparent=False)
