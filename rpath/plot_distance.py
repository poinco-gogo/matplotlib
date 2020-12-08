import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('classic')

nrep = 32

for i in range(1, 33):
	f = str(i) + ".pathcv"
	d = np.loadtxt(f, usecols=2)
	hist, bins = np.histogram(d, range=(0, 1000), bins=101, density=True)
	x = []
	for i in range(1,len(bins)):
		x.append((bins[i-1] + bins[i]) * 0.5)
	plt.plot(x, hist, alpha=0.6)

plt.xlabel("Distance [A]")
plt.ylabel("Density")
plt.grid()
plt.tight_layout()
plt.savefig("tmp.png", dpi=300, Transparent=True)
