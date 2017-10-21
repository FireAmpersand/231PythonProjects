def sum(a,b,c):
	"Returns the sum of a,b,c"
	sum = a + b + c
	return sum

def testNums(a,b,c):
	"Testing if numbers are the same"
	a2 = 0
	b2 = 0
	c2 = 0
	if ((a != b) and (b != c) and (c != a)):
		a2 = a
		b2 = b
		c2 = c
	elif (a == b and c != b):
		c2 = c
	elif (a != b and b == c):
		a2 = a
	elif (a == c and b != a):
		b2 = b
	return(a2,b2,c2)

a = int(input("Enter First: "))
b = int(input("Enter Second: "))
c = int(input("Enter Third: "))

d,e,f = testNums(a,b,c)
s = sum(d,e,f)
print(s)
