import pygame
import rushhour
#from PyZenity import *

def main():
	"Sets up the game and runs the game"
	#Starting the pygame
	pygame.init()
	#HOw many sqaures per row/column
	gameSquares = 6
	#The Variable holding square size
	gameSquareSize = 150
	#Varible to change screen size
	surfaceSize = gameSquareSize * gameSquares
	#Setting up the window size
	gameBoard = pygame.display.set_mode((surfaceSize,surfaceSize))
	#The defualt colors of the squares and thier border
	defaultSquareColor = (255,255,255)
	defaultBorderColor = (0,0,0)
	#Creating a backend object
	gameBackend = rushhour.Board()
	#Loading in a game to play
	gameBackend.loadGame()
	#Variables
	mouseClickOneLoc = ""
	mouseClickTwoLoc = ""
	gameBackend.updateBoard()
	turns = 0
	while True:
		#Running an event check
		ev = pygame.event.poll()
		#If the window close event comes through, break out of the loop
		if ev.type == pygame.QUIT:
			break
		#Checking to see if the game has been won
		if gameBackend.gameWon(turns) == 1:
			InfoMessage("You Won in {0} turns".format(turns))
			break
		#If a mouse click event comes through, record location and click numbers
		if ev.type == pygame.MOUSEBUTTONDOWN:
			#Testing if it is the first click
			if mouseClickOneLoc == '' and mouseClickTwoLoc == "":
				#Getting the position of the click
				mouseClickOneLoc = ev.dict['pos']
				#Changing the varible into a form that the backend understands (from pixels to squares)
				mouseClickOneLoc = [int(mouseClickOneLoc[0] / gameSquareSize), int(mouseClickOneLoc[1] / gameSquareSize)]
			#Testing to see if it is the second click
			elif mouseClickOneLoc != '' and mouseClickTwoLoc == "":
				#Getting the position of the click
				mouseClickTwoLoc = ev.dict['pos']
				#Changing the varible into a form the backend can understand (from pixels to squares)
				mouseClickTwoLoc = [int(mouseClickTwoLoc[0] / gameSquareSize), int(mouseClickTwoLoc[1] / gameSquareSize)]
				#Finding which car has been selected, calls the beckend to do a reverse lookup of the car
				selectedCar = gameBackend.reverseCarLookup(mouseClickOneLoc)
				#Calculating the differences between squares
				xDifference = int(mouseClickTwoLoc[0]) - int(mouseClickOneLoc[0])
				yDifference = int(mouseClickTwoLoc[1]) - int(mouseClickOneLoc[1])
				#Checking if the requested move is a vertical move
				if mouseClickTwoLoc[0] == mouseClickOneLoc[0] and mouseClickTwoLoc[1] != mouseClickOneLoc[1]:
					#Creating a direction variable
					direction = ""
					#If the y difference is negative, movement is then up
					try:
						if yDifference < 0:
							direction = "up"
							mouseClickOneLoc = gameBackend.cars[selectedCar].blocking[0]
							yDifference = int(mouseClickTwoLoc[1]) - int(mouseClickOneLoc[0])
						#If the y difference is positive, movement is then down
						elif yDifference > 0:
							direction = "down"
							mouseClickOneLoc = gameBackend.cars[selectedCar].blocking[len(gameBackend.cars[selectedCar].blocking) - 1]
							yDifference = int(mouseClickTwoLoc[1]) - int(mouseClickOneLoc[0])
						#The amount to move is just the absolute value of the direction
						amount = abs(yDifference)
						#Send the move information to the backend for processing
						gameBackend.checkValidMove(selectedCar, direction, amount)
						#After move has been processed, update the internal board
						gameBackend.updateBoard()
						#Adds 1 to the turn count
						turns += 1
					except:
						#ErrorMessage("Invalid Move")
						print("Invaild Move")
				#Checking if the reqested move is a horizontal move
				elif mouseClickTwoLoc[0] != mouseClickOneLoc[0] and mouseClickTwoLoc[1] == mouseClickOneLoc[1]:
					#Creating a direction variable
					direction = ""
					try:
						#If the x difference is negative, movement is then left
						if xDifference < 0:
							direction = "left"
							mouseClickOneLoc = gameBackend.cars[selectedCar].blocking[0]
							xDifference = int(mouseClickTwoLoc[0]) - int(mouseClickOneLoc[1])
						#If x difference is positive, movement is then right
						elif xDifference > 0:
							direction = "right"
							mouseClickOneLoc = gameBackend.cars[selectedCar].blocking[len(gameBackend.cars[selectedCar].blocking) - 1]
							xDifference = int(mouseClickTwoLoc[0]) - int(mouseClickOneLoc[1])
						#The amount is just the absolute value of the x Difference
						amount = abs(xDifference)
						#Sending the information to the backend for processing
						gameBackend.checkValidMove(selectedCar, direction, amount)
						#Adds 1 to the turn count
						turns += 1
					except:
						#ErrorMessage("Invalid Move")
						print("Invaild Move")
					#After move has been processed, update the internal board
					gameBackend.updateBoard()
				#Resetting the varibles after being used
				mouseClickOneLoc = ''
				mouseClickTwoLoc = ''
			elif mouseClickOneLoc != '' and mouseClickTwoLoc != "":
				print("FAIL SAFE")
				mouseClickOneLoc = ""
				mouseClickTwoLoc = ""
		#Updating the squares on the board
		grid = []
		#Looping through each row
		for row in range(gameSquares):
			#Resetting the temp list every loop iteration
			temp = []
			#Creating the individual sqaures in the row
			for col in range(gameSquares):
				#Creating the the square being changed
				currentSquare = pygame.Rect(col * gameSquareSize, row * gameSquareSize, gameSquareSize, gameSquareSize)
				#Changes the current squares color and adds a border
				drawRect(gameBoard, defaultSquareColor,defaultBorderColor, currentSquare)
				#Adds the square to the temp list
				temp.append(currentSquare)
			#Adding the row to the grid
			grid.append(temp)
		#Looping through the cars, getting thier locations and colors and changing the squares the car is on
		for i in range(gameBackend.totalCars):
			#Getting the current car
			currentCar = gameBackend.cars[i]
			#Getting the car's location
			currentCarLocation = currentCar.blocking
			#Getting the car's color
			currentCarColor = currentCar.color
			#Looping through the size of the car
			for loc in range(len(currentCarLocation)):
				#Changing the color of a sqaure that has a car on top of it
				drawRect(gameBoard,currentCarColor, defaultBorderColor, grid[currentCarLocation[loc][0]][currentCarLocation[loc][1]])
		pygame.display.update()


def drawRect (surface, rectColor, borderColor, rect, border=1):
	"Draws a rectangle with a boarder around it"
	#Draws the boarder square first with default size
	surface.fill(borderColor, rect)
	#Then fills in the selected color with a small size change
	surface.fill(rectColor, rect.inflate(-border*2, -border*2))


if __name__ == "__main__":
	main()
