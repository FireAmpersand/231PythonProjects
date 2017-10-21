def sum(a,b,c):
	return a + b + c

def test(a,b,c):
	a2 = a
	b2 = b
	c2 = c
	if (a <= 19 and a >= 13):
		a2 = 0
	if (b <= 19 and b >=13):
		b2 = 0
	if (c <= 19 and c >=13):
		c2 = 0
	if (a - b == 1 or a - b == -1):
		a2 = 0
		b2 = 0
	elif (b - c == 1 or b - c == -1):
		b2 = 0
		c2 = 0
	elif (c - a == 1 or c - a == -1):
		a2 = 0
		c2 = 0
	return(a2,b2,c2)

a = int(input("1: "))
b = int(input("2: "))
c = int(input("3: "))

d,e,f = test(a,b,c)
print(sum(d,e,f))
