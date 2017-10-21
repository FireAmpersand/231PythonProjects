a = int(input("Enter A: "))

for x in range(1, 1000):
	for z in range (1,1000):
		y = a
		if x*x == y*y + z*z:
			if y < z < x:
				print(y,z,x)


