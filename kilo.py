small = 1
large = 5

def package(x):
	totalLarge = int( (x / 5))
	totalSmall = x - (totalLarge * 5)
	if (totalLarge <= 0 and totalSmall <=0):
		print(-1)
		return
	print("Smalls: " + str(totalSmall)  + ", Larges: " + str(totalLarge))

num = int(input("Number: "))
package(num)
