import sys

nbias = 32
ndim  = 286 * 3
with open(sys.argv[1], mode='r') as f:
	l = f.readlines()
	for i in range(0, ndim):
		s = str(i + 1) + " "
		print(s, end="")
		for j in range(0, nbias):
			print(l[3*i+1].split()[j+2],end="")
			print(" " ,end="")
		for j in range(0, nbias):
			print(l[3*i+1].split()[j+2],end="")
			print(" " ,end="")
		for j in range(0, nbias):
			print(l[3*i+1].split()[j+2],end="")
			print(" " ,end="")
		print("")
		
	
