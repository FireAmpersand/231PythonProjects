def findSnakes():
	"Checks if snakes is in the current line, if so print the line"
	fileIn = open("test.txt", "r")
	while True:
		s = fileIn.readline()
		if("snake" in s):
			print(s)
		if (len(s) == 0):
			break

findSnakes()
