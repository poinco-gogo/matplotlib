import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

mpl.style.use('classic')
#mpl.rcParams['font.family'] = 'Arial'
#mpl.rcParams["mathtext.rm"] = 'Arial'

labels = ['405-410 ns', '385-390 ns', '365-370 ns', '345-350 ns', '325-330 ns', '305-310 ns', '285-290 ns', '265-270 ns', '245-250 ns', '225-230 ns', '205-210 ns', '185-190 ns', '165-170 ns', '145-150 ns', '125-130 ns', '105-110 ns', '85-90 ns', '65-70 ns', '45-50 ns']

nrep = 32
num = np.arange(34, 107, 4)
for k in range(0, len(num)):
	rmsd = []
	for irep in range(1, nrep+1):
		fname = "../simanl_004_eq" + "{0:03d}".format(num[k]) + "/output/" + str(irep) + ".nwt.rmsd_eq"
		with open(fname) as f:
			s = f.readlines()
			r = float(s[17].split()[1])
			rmsd.append(r)
	dx = np.arange(1,33)
	dy = rmsd
	plt.plot(dx, dy, color=cm.cool(float(k)/len(num)), label=labels[len(num) - 1 - k])

plt.xticks([1,4,8,12,16,20,24,28,32])
plt.xlim([1, 32])
plt.xlabel("Image index",fontsize=18)
plt.ylabel("RMSD ($\AA$)",fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
#sm = plt.cm.ScalarMappable(cmap=cm.jet, norm=plt.Normalize(vmin=0.1, vmax=ndat*ndir))
#sm._A = []
#plt.colorbar(sm)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=10)
plt.tight_layout()
plt.savefig("tmp.eps",dpi=300,transparent=True)
plt.show()
