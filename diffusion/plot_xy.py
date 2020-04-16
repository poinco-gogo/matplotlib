import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

mpl.style.use('classic')
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams["mathtext.rm"] = 'Arial'

def plot_xy_projections(aa, irep):
	aa.get_xaxis().set_tick_params(direction='in')
	aa.get_yaxis().set_tick_params(direction='in')
	for tick in aa.yaxis.get_major_ticks():
		tick.label.set_fontsize(16)
	for tick in aa.xaxis.get_major_ticks():
		tick.label.set_fontsize(16)
	aa.set_xlim([-70,70])
	aa.set_ylim([-70,70])
	if (irep % 3 == 1):
		aa.set_ylabel('Y (angs.)', fontsize=18)
	if ((irep > 3 and irep < 7) or irep > 9):
		aa.set_xlabel('X (angs.)', fontsize=18)
	title = "Replica #" + str(irep)
	aa.set_title(title, fontsize=16)
	fname = "21-50_" + str(irep) + ".log_hemePosition"
	d  = np.loadtxt(fname, comments="REMARK")
	x  = d[:,11]
	y  = d[:,12]
	aa.set_aspect('equal','box')
	aa.plot(x, y, marker='.')


# for replica 1 to 6
fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(8, 6), sharex=True, sharey=True)

for i in range(0, 2):
	for j in range(0, 3):
		plot_xy_projections(ax[i][j], 3 * i + j + 1)

plt.tight_layout()
fname2 = "tmp_1-6.eps"
plt.savefig(fname2,dpi=300,transparent=True)

# for replica 7 to 12
fig2, ax2 = plt.subplots(nrows=2, ncols=3, figsize=(8, 6), sharex=True, sharey=True)

for i in range(0, 2):
	for j in range(0, 3):
		plot_xy_projections(ax2[i][j], 3 * i + j + 1 + 6)

plt.tight_layout()
fname2 = "tmp_7-12.eps"
plt.savefig(fname2,dpi=300,transparent=True)
