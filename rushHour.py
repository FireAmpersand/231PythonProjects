import sys

class Cars:
	"Creates and holds the cars location and direction"

	def __init__ (self, direction, size, upMostCoor, leftMostCoor):
		"Creates a new cars object"
		self.direction = direction
		self.blocking = []
		#Finding which Coordinates the car is blocking
		if (self.direction == 'h'):
			for i in range(int(size)):
				#If horizontal, loop 2/3 times (Based on size) to find other xCoordinates
				self.blocking.append([int(upMostCoor),int(leftMostCoor) + i])
		else:
			for i in range(int(size)):
				#If vertical, loop 2/3 times (Based on size) to find other yCoordinates
				self.blocking.append([int(upMostCoor) + i, int(leftMostCoor)])

	def moveCar(self, direction, amount):
		"Changes the cars current position"
		#Setting the old locations
		oldLocation = self.blocking
		#Resetting the blocking list
		self.blocking = []
		#Checks if the car and move horizontaly or verticaly
		if (self.direction == 'h'):
			#Checks the direction it is moving
			if(direction == 'left'):
				#Loops through the length of the car, moving all x values left
				for i in range(len(oldLocation)):
					self.blocking.append([oldLocation[0][0], oldLocation[i][1] - amount])
			if(direction == "right"):
				#Loops through the length of the car, moving all the x values right
				for i in range(len(oldLocation)):
					self.blocking.append([oldLocation[0][0], oldLocation[i][1] + amount])
		if (self.direction == 'v'):
			#Checks the direction it is moving
			if (direction == "up"):
				#Loops through the length of the car, moving all y values "up" (down as 0,0 is top left)
				for i in range(len(oldLocation)):
					self.blocking.append([oldLocation[i][0] - amount, oldLocation[0][1]])
			if(direction == "down"):
				#Loops through the length of the car, moving all y values "down" (up as 0,0 is top left)
				for i in range(len(oldLocation)):
					self.blocking.append([oldLocation[i][0] + amount, oldLocation[0][1]])


class Board:
	"Creates a Board Object"

	def __init__(self, cars):
		"Takes in all the cars, and places them on the board"
		self.totalCars = len(cars)
		self.cars = cars

	def displayBoard(self):
		"prints out the game board to the terminal"
		self.board = []
		#Setting every position to the defualt '*'
		#Row loop
		for row in range(6):
			#Column loop
			temp = []
			for col in range(6):
				temp.append("*")
			self.board += [temp]

		#Adding in the cars to the board
		for i in range(self.totalCars):
			#Selcting the current car
			currentCarLocations = self.cars[i].blocking
			for a in range(len(currentCarLocations)):
				#Selecting the current Coordinate being inspected
				currentInspecting = currentCarLocations[a]
				#Getting the xCoor out of the Coordinate Pair
				xLoc = currentInspecting[1]
				#Getting the yCoordinate out of the Coordinate Pair
				yLoc = currentInspecting[0]
				#Setting the board location to the cars number
				self.board[yLoc][xLoc] = i

		#Printing out the board to the terminal
		#Looping through the rows
		for row in range(6):
			#Looping through the columns
			for col in range(6):
				#Printing out the value on the same line
				print(self.board[row][col], end=" ")
			#Creating a new line
			print("")

	def checkValidMove(self,car,direction,amount):
		"Checks to make sure the reqested move is vaild"
		car = int(car)
		amount = int(amount)
		#Getting car's Locations and direction
		currentCarLocation = self.cars[car].blocking
		currentCarDirection = self.cars[car].direction
		#Checking if the direction matches the the car's direction
		if( (direction == 'left' or direction == 'right') and currentCarDirection == 'v'):
			#If the movement is horizontal and the car is a vertical, cancel movement and print Invalid text
			print("Invalid move, cars can only move in the directions they are facing")
			return
		elif( (direction == 'up' or direction == 'down') and currentCarDirection == 'h'):
			#If the movement is vertical and the car is horizontal, cancel movement and print invalid text
			print("Invalid move, cars can only move in the direction they are facing")
			return
		#If the direction is correct, then test any points in the path of the movement
		else:
			#Running the Car's move function to know the new location Coordinates
			self.cars[car].moveCar(direction,amount)
			#Creating a new varible to hold the final positions
			newPossibleLocation = self.cars[car].blocking
			#Reseting the car's location back to what it was before
			self.cars[car].blocking = currentCarLocation
			#Looping through each coorinate pair
			i = 0
			if(direction == 'right' or direction == 'down'):
				i = len(newPossibleLocation)-1
			#Getting the current row and column in question
			row = newPossibleLocation[i][0]
			col = newPossibleLocation[i][1]
			#Checking if the new location is in bounds
			if ( row < 0 or row > 5):
				print("Out of bounds")
				return
			elif( col < 0 or col > 5):
				print("Out of Bounds")
				return
			#Checking if the car has a clear path to its new location
			moveCheck = self.slideCheck(currentCarLocation, direction,amount)
			if(moveCheck == "false"):
				print("Invalid Move, Car in the Way")
				return
			#Checking if the new location is empty
			if (self.board[row][col] != "*"):
				print("Invalid Move, Car At Location")
				return
			#If no flags get triped, then the new location is set with a board update
			self.cars[car].blocking = newPossibleLocation


	def slideCheck(self, startLocations, direction, amount):
		"Runs a check to make sure that cars can't jump over another"
		if (direction == 'left'):
			#Looping for how ever much the car is moving
			for move in range(amount):
				#Setting the x,y - coordinates for the current point
				ghostMoveY = startLocations[0][0]
				ghostMoveX = startLocations[0][1] - (move + 1)
				#If the point along the slide is not empty, return a false
				if(self.board[ghostMoveY][ghostMoveX] != "*"):
					return("false")
			#If all loop iteration pass, then return a true
			return("true")

		elif(direction == 'right'):
			#Looping for how ever much the car is moving
			for move in range(amount):
				#Setting the x,y - coordinates for the current point
				ghostMoveY = startLocations[len(startLocations)-1][0]
				ghostMoveX = startLocations[len(startLocations)-1][1] + move + 1
				#If the point along the slide is not empty, return false
				if(self.board[ghostMoveY][ghostMoveX] != "*"):
					return("false")
			#If all loop iteration pass, return true
			return("true")

		elif(direction == 'up'):
			#Looping for how ever much the car is moving
			for move in range(amount):
				#Setting the x,y coordinates for the current point
				ghostMoveY = startLocations[0][0] - (move + 1)
				ghostMoveX = startLocations[0][1]
				#If the point along the slide is not empty, return false
				if(self.board[ghostMoveY][ghostMoveX] != "*"):
					return("false")
			#If all loop iterations pass, return true
			return("true")

		elif(direction == 'down'):
			#Looping for how ever much the car is moving
			for move in range(amount):
				#Setting the x,y - coordinates for the current point
				ghostMoveY = startLocations[len(startLocations)-1][0] + move + 1
				ghostMoveX = startLocations[len(startLocations)-1][1]
				#If the point along the slide is not empty, return false
				if(self.board[ghostMoveY][ghostMoveX] != "*"):
					return("false")
			#If all loop iterations pass, return true
			return("true")

	def gameWon(self, turns):
		"Checks if the game has been won"
		redCarLocation = self.cars[0].blocking
		if(redCarLocation[1][0] == 2 and redCarLocation[1][1] == 5):
			print("You Won in {0} Turns".format(turns))
			return 1
		return 0

	def inputGameFile(self):
		"Inputs a game board from a file, returns the list of cars"
		inputList = []
		while(1==1):
			#Runs an infinite loop untill broken out of dure to no more text
			

def main():
	"The function that runs the game"
	#Setting variables for the game
	gameBoard = gameSetup()
	gameBoard.displayBoard()
	gameOver = 0
	turns = 0
	#Game loop
	while(gameOver == 0):
		#Asking inputs 
		carChoice = askCarNumber(gameBoard)
		direction = askCarDirection(gameBoard,carChoice)
		units = askAmountToMove()
		gameBoard.checkValidMove(carChoice,direction,units)
		gameBoard.displayBoard()
		turns += 1
		gameOver = gameBoard.gameWon(turns)


def askAmountToMove():
	"A Function used to ask how much the player would like to move the car"
	units = input("How many units? ")
	try:
		units = int(units)
		if(units < 0 or units > 4):
			print("Please enter a number between 0-4")
			return askAmountToMove()
		return units
	except ValueError:
		print("Please enter a integer")
		return askAmountToMove()


def askCarDirection(gameBoard, car):
	"A Function used to ask which way the player would like to move the car"
	carDirection = gameBoard.cars[car].direction
	carText = ""
	if(carDirection == "v"):
		carText = "up, down"
	elif(carDirection == 'h'):
		carText = "left, right"
	direction = input("Which way would you like to move? ({0}) ".format(carText))
	direction = direction.lower()
	if(carDirection == 'v' and (direction != "up" and direction != "down")):
		print("Please enter up or down")
		return askCarDirection(gameBoard, car)
	if(carDirection == 'h' and (direction != "left" and direction != "right")):
		print("Please enter left or right")
		return askCarDirection(gameBoard, car)
	return direction


def askCarNumber(gameBoard):
	"A Function used to ask which car they would like move"
	carChoice = input("Please select a car to move ")
	try:
		carChoice = int(carChoice)
		if(carChoice < 0 or carChoice > len(gameBoard.cars) -1):
			print("Please enter a int in the range of 0 - {0}".format(len(gameBoard.cars)-1))
			return askCarNumber(gameBoard)
		return carChoice
	except ValueError:
		print("Enter a valid Int Please")
		return askCarNumber(gameBoard)

def gameSetup():
	"Takes the imported board specs, and creates the car objects. Returns all cars"
	inputList = []
	gameFile = open(sys.argv[1],'r')
	while(1==1):
		#Runs a infinite loop untill broken out of, looping through all inputs
		currentLine = (gameFile.readline())
		if(len(currentLine) == 0):
			break
		currentCar = [currentLine] #Sets the temp list to the inputed value
		#Adds the current car to the main list
		inputList += [currentCar]
	gameFile.close()

	cars = []
	#Loops through all inputs and creates cars objects
	for i in range(len(inputList)):
		#Splits the inputed text into a list
		temp = inputList[i][0].split(', ')
		#Creating the current car object
		current = Cars(temp[0],temp[1],temp[2],temp[3])
		#Adding the new car to the list
		cars.append(current)

	return Board(cars)


main()
