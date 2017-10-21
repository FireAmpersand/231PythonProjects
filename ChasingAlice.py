import turtle
import random
import math
##########################################################
#		Made By Zachary Passmore		 #
#			30043532			 #
#		  Computer Science 231			 #
#########################################################

def moveAlex(alex,alice):
	"Moves the player's turtle (Alex)"
	inpt = input("Alex's Move: ")
	inpt = inpt.lower()
	if (inpt == "w"):
		#Moves Alex Forward
		alex.forward(30)
		checkIsInBounds(alex,alice)
	elif(inpt == "d"):
		#Turns Alex to the right
		alex.right(45)
	elif(inpt == "a"):
		#Turns Alex to the left
		alex.left(45)
	elif (inpt == "s"):
		#Moves Alex Backwards
		alex.forward(-30)
		checkIsInBounds(alex,alice)
	else:
		#Edge case, where the player inputs a incorrect letter, reruns moveAlex
		print("W,A,S,D, Only")
		moveAlex(alex,alice)
def moveAlice(alice,alex):
	"Moves the computer's turtle"
	moveChoice = math.floor(random.random() *3) #Random movement generator
	if(moveChoice == 0 or moveChoice == 1): #Has a 2/3 chance of moving forward rather than turning
		alice.forward(20)
		checkIsInBounds(alice,alex)
	elif(moveChoice == 2): # Has a 1/3 chance of turning rather than moving
		direction = math.floor(random.random() *2) #Random number between 0-1 for turn direction
		if (direction == 0):
			alice.left(90)
		else:
			alice.right(90)

def randomSpawnGeneration(turtle,opponent):
	"Chooses a random location on the board within window settings and not in a win condition"
	xLoc = math.floor(random.random()*500) #Generates a number between 0 - 500 for the x
	yLoc = math.floor(random.random()* 500) #Generates a number between 0 - 500 for y

	if((opponent.xcor()-30) <= xLoc <= (opponent.xcor()+30) and (opponent.ycor()-30) <= yLoc <= (opponent.ycor()+30)):
		 #Checks to see if it is spawning in a win condition
		randomSpawnGeneration(turtle,opponent)
	#Moving the turtle to the random location
	turtle.penup()
	turtle.speed(0)
	turtle.goto(xLoc,yLoc)
	turtle.speed(5)
	turtle.pendown()

def checkIsClose(alex,alice): # Will Return a boolean if alex is close to alice
	"Checks to see if Alex is 30 pixels away from Alice"
	#Getting the distance between the turtles on the X-axis
	xDistance = abs(alex.xcor()-alice.xcor())
	yDistance = abs(alex.ycor() - alice.ycor())
	if(xDistance <= 30 and yDistance <= 30):
		return("true")
	else:
		return("false")

def checkIsInBounds(turtle,opponent):
	"Checks if the turtle's new location is within the window"
	turLocX, turLocY = turtle.pos() #Gets the position of the turtle in question
	if(turLocX < 0 or turLocX > 500):
		#Checks if x is out of bounds, if so, generates a random spawn and ends the check
		randomSpawnGeneration(turtle,opponent)
		return
	elif(turLocY < 0 or turLocY > 500):
		#Checks if y is out of bounds, if so, generates a random spawn and ends the check
		randomSpawnGeneration(turtle,opponent)
		return

def stepDisplayUpdate(stepCount,step,alex,alice):
	"Updates the step text at the top of the screen"
	step.clear()
	#Removes the old text to be replaced by the new text

	alexX,alexY = alex.position()
	aliceX, aliceY  = alice.position()
	#Getting Alex and Alice's Locations

	xDisplacement = abs(alexX - aliceX)
	yDisplacement = abs(alexY - aliceY)
	diagonalDisplacement = math.floor(((xDisplacement ** 2) + (yDisplacement **2) )**(0.5))
	#Calculatng the Distance Between Alex And Alice

	if(checkIsClose(alex,alice) == "true"):
		#Checking If the game has been won, if so print a win message with total steps
		step.write("You Caught Alice In {0} Turns!".format(stepCount))
	else:
		#If the statment is not true, output the step counter and distance
		step.write("Step {0}: Alex is {1} pixels from Alice".format(stepCount,diagonalDisplacement))

def gameSetup(windowSize):
	"Sets up the game objects and world"
	#Screen Setup
	wn = turtle.Screen()
	wn.setworldcoordinates(0,0,windowSize,windowSize) #Sets the origin to bottom left so that all numbers are positive

	#Alex Setup
	alex = turtle.Turtle()
	alex.speed(0)
	alex.color("blue")
	alex.penup()
	alex.goto(250,250)
	alex.speed(5)
	alex.pendown()
	alex.shape("turtle")

	#Alice Setup
	alice = turtle.Turtle()
	alice.color("red")
	randomSpawnGeneration(alice,alex)
	alice.shape("turtle")

	#Step Counter Setup
	step = turtle.Turtle()
	step.shape("blank")
	step.penup()
	step.pensize(6)
	step.speed(0)
	step.goto(0,490)
	step.write("Step 0: Game Setup")

	#Returns all game objects that need to be called outside this method
	return(wn,alex.getturtle(),alice.getturtle(),step.getturtle())

def main():
	"The Primary Method for running everything"
	windowSize = 500
	stepCount = 0
	wn, alex,alice,step = gameSetup(windowSize)
	#Game While Loop, Runs until checkIsClose is false.
	#Checks if won -> Moves Alex -> Checks if won -> Move Alice -> Updates display -> Loop
	while (checkIsClose(alex,alice) == "false"):
		moveAlex(alex,alice) #Alex's Move
		if (checkIsClose(alex,alice) == "true"): #Checks Win Condition
			stepCount = stepCount + 1
			stepDisplayUpdate(stepCount,step,alex,alice) #Updates Text
			break
		moveAlice(alice,alex) #Alice's Move
		stepCount = stepCount + 1
		stepDisplayUpdate(stepCount,step,alex,alice) #Updates Text

	wn.mainloop()

main()
