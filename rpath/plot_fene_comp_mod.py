import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm     as cm

mpl.style.use('classic')
#mpl.rcParams['font.family'] = 'Arial'
#mpl.rcParams["mathtext.rm"] = 'Arial'

paths = ['fene1.dat', '../../../simanl_004_eq066/output/mbar_analysis/fene1.dat', '../../../simanl_004_eq062/output/mbar_analysis/fene1.dat', '../../../simanl_004_eq058/output/mbar_analysis/fene1.dat', '../../../simanl_004_eq054/output/mbar_analysis/fene1.dat', '../../../simanl_004_eq050/output/mbar_analysis/fene1.dat', '../../../simanl_004_eq046/output/mbar_analysis/fene1.dat', '../../../simanl_004_eq042/output/mbar_analysis/fene1.dat', '../../../simanl_004_eq038/output/mbar_analysis/fene1.dat', '../../../simanl_004_eq034/output/mbar_analysis/fene1.dat', '../../../simanl_004_eq030/output/mbar_analysis/fene1.dat', '../../../simanl_004_eq005/output/mbar_analysis/fene1.dat']

labels = ['225-230 ns', '205-210 ns', '185-190 ns', '165-170 ns', '145-150 ns', '125-130 ns', '105-110 ns', '85-90 ns', '65-70 ns', '45-50 ns', '25-30 ns', '0-5 ns']


def load_fene(path):
	data = np.loadtxt(path, comments="REMARK")
	x    = data[:, 0]
	y    = data[:, 1]
	piv  = 9999
	for i in range(0, 32):
		if y[i] < piv:
			piv = y[i]
	for i in range(0, 32):
		y[i] -= piv
	return x, y

def plot_line(path, label, ratio):
	x = []
	y = []
	x, y = load_fene(path)
	plt.plot(x,y,lw=2, marker='o',label=label,color=cm.cool(ratio))


for i in range(0, len(paths)):
	plot_line(paths[i], labels[i], float(i+1)/len(paths))


plt.xlabel("Image index",fontsize=18)
plt.ylabel("Free energy (kcal/mol)",fontsize=18)
plt.xlim([0,33])
plt.xticks([1,4,8,12,16,20,24,28,32])
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.legend(loc='upper left')
plt.grid()
plt.tight_layout()
plt.savefig("tmp.eps",dpi=300,Transparent=True)
