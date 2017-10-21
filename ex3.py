import sys

def test(did_pass):
	" Prints the result of the test"
	linenum = sys._getframe(1).f_lineno
	if (did_pass):
		msg = "Test at line {0} ok".format(linenum)
	else:
		msg  ="Test at line {0} FAIL".format(linenum)
	print(msg)

def turn_clockwise(direction):
	"Returns The Direction Clockwise of The original"
	if (direction == "N"):
		return "E"
	elif(direction == "E"):
		return "S"
	elif(direction == "S"):
		return "W"
	elif(direction == "W"):
		return "N"


def grade(mark):
	"Returns The Grade"
	if(mark >= 75):
		return "First"
	elif(mark >= 70 and mark < 75):
		return "Upper Second"
	elif(mark >= 60 and mark < 70):
		return "Second"
	elif(mark >= 50 and mark < 60):
		return "Third"
	elif(mark >= 45 and mark < 50):
		return "F1 Supp"
	elif(mark >= 40 and mark < 45):
		return "F2"
	elif(mark > 40):
		return "F3"

def test_suite():
	test(turn_clockwise("N") == "E")
	test(turn_clockwise("E") == "S")
	test(turn_clockwise("S") == "W")
	test(turn_clockwise("W") == "N")
	test(turn_clockwise(1) == None)

dir = input("Enter The Direction As A Letter ")
print(turn_clockwise(dir))

gra = float(input("Enter Grade: "))
print( str(gra) + ":" + str( grade(gra) ) )
