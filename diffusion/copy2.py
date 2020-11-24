rpath = "step01.sh"
for i in range(2, 99):
	k = "{0:02d}".format(i)
	wpath = "step" + k + ".sh"
	with open(rpath) as f1:
		l = f1.readlines()
		l[10] = "#PJM -o step" + k + ".out\n"
		l[15] = "mpirun -np 32 -ppn 8 /home/ktamu/sugitalab/genesis-1.4.0dev/bin/spdyn step" + k + ".inp\n"
		with open(wpath, mode='w') as f2:
			f2.writelines(l)
