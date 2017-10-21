def solve(x):
	if(x % 10 <=4):
		print(x - (x % 10))
	else:
		print(x + 10 - (x %10))

num =  int(input("Number: "))
solve(num)
