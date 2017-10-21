input(">>>>>")
start = 020131452
sum = 0
numbers = [""]
for i in range (10):
	x = start %10 
	start = start/ 10
	print(i,x)
	sum = sum + i*x

if (sum %11 == 0):
	d1 = 0
else:
	d1 = (sum%11) 
