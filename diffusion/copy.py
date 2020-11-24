rpath = "step01.inp"
for i in range(2, 99):
	j = "{0:02d}".format(i - 1)
	k = "{0:02d}".format(i)
	t1 = 310.0 + 5.0 * i
	if (t1 >= 500.0):
		t1 = 500.0
	t2 = 310.0 + 5.0 * i
	wpath = "step" + k + ".inp"
	with open(rpath) as f1:
		l = f1.readlines()
		l[10] = "rstfile = output/step" + j + "_{}.rst\n"
		l[13] = "dcdfile = output/step" + k + "_{}.dcd\n"
		l[14] = "rstfile = output/step" + k + "_{}.rst\n"
		l[15] = "remfile = output/step" + k + "_{}.rem\n"
		l[16] = "logfile = output/step" + k + "_{}.log\n"
		l[24] = "parameters1      = " + str(t1) + " " + str(t2) + "\n"
		with open(wpath, mode='w') as f2:
			f2.writelines(l)
