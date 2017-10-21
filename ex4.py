def print_triangular_number(n):
	i = 1
	while(i < n + 1):
		j = 1
		count = 0
		while (j < i + 1):
			count = count + j 
			j = j + 1
		print(i, "\t",count)
		i = i + 1


def num_digits(n):
	n = abs(n)
	if (n == 0):
		return(1)
	else:
		return(len(str(n)))

def testSuite():

	print("Triangular Numbers")
	print_triangular_number(5)
	print("Number of Digits")
	print(0,"\t",num_digits(0))
	print(-12345, "\t", num_digits(-12345))

testSuite()
