import sys

ndim  = 286 * 3
with open(sys.argv[1], mode='r') as f:
	l = f.readlines()
	for i in range(0, ndim):
		print(l[3 * i    ], end="")
		print(l[3 * i + 1], end="")
		print("is_periodic" + str(i+1) + " = NO")
		print("")
		
	
