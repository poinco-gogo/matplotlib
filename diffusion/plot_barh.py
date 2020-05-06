import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [5.07e-7, 5.25e-7, 6.16e-7, 5.52e-7]
label_x = ["MD","gREST 02","gREST 04", "gREST 05"]

plt.barh(x, y, align="center")
plt.gca().ticklabel_format(style="sci", scilimits=(0,0), axis="y")
plt.yticks(x, label_x)
plt.xlabel("Diffusion coefficient [cm2/s]")
plt.show()
plt.savefig("tmp.eps",dpi=300,transparent=True)
