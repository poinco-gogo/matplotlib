import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('classic')
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams["mathtext.rm"] = 'Arial'

fig, ax = plt.subplots(nrows=4, ncols=3, figsize=(16,12),sharex=True)

def plot_msd(aa, irep):
	aa.get_xaxis().set_tick_params(direction='in')
	aa.get_yaxis().set_tick_params(direction='in')
	for tick in aa.yaxis.get_major_ticks():
		tick.label.set_fontsize(20)
	for tick in aa.xaxis.get_major_ticks():
		tick.label.set_fontsize(20)
	aa.set_xlim([0,1000])
	if (irep % 3 == 1):
		aa.set_ylabel('MSD (angs.2)', fontsize=20)
	if (irep > 9):
		aa.set_xlabel('Time (ps)', fontsize=20)
	title = "Replica #" + str(irep)
	aa.set_title(title, fontsize=16)
	fname = str(irep) + ".msd"
	d  = np.loadtxt(fname, usecols=(0,1), comments="REMARK")
	x = d[:,0][::5] * 10
	y = d[:,1][::5]
	aa.scatter(x, y, color='#1f77b4', marker='o', s=80, facecolor='white')
	aa.grid(which='both',linestyle='--',linewidth=0.5)
	fname = str(irep) + ".log"
	d = 0.0
	with open(fname) as f:
		s = f.readlines()
		a = float(s[4].split()[3]) * 0.1
		b = float(s[5].split()[3])
		d = float(s[7].split()[5])
		xx = np.arange(200,1001)
		yy = a * xx + b
		aa.plot(xx, yy, color='blue')
	aa.set_ylim(bottom=0)
	return d

vave = 0.0
for i in range(0, 4):
	for j in range(0, 3):
		vave += plot_msd(ax[i][j], 3 * i + j + 1)
print (vave / 12.0)

#plt.legend(loc="best")
plt.tight_layout
plt.savefig("tmp.eps", dpi=300)
