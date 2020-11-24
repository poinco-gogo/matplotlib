import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [3.97e-6, 4.46e-6, 4.93e-6, 4.10e-6, 9.39e-6, 8.58e-6, 5.63e-6, 5.83e-6, 4.31e-6, 5.78e-6, 2.08e-6, 1.86e-6]
label_x = ["Sim01#1", "Sim01#2", "Sim02#1", "Sim02#2", "Sim03#1", "Sim03#2", "Sim04#1", "Sim04#2", "Sim05#1", "Sim05#2", "Sim06#1", "Sim06#2"]

plt.figure(figsize=(4.0, 3.0))

plt.barh(x, y, align="center")
plt.gca().ticklabel_format(style="sci", scilimits=(0,0), axis="x")
plt.yticks(x, label_x)
plt.xlabel("Diffusion coefficient [cm2/s]")
plt.tight_layout()
plt.show()
plt.savefig("tmp.eps",dpi=300,transparent=True)
