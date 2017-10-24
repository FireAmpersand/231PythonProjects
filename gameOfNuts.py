###################################
#	  Zachary Passmore	  #
#	      30043532		  #
#	      CPSC 231		  #
###################################

def main():
	"The Main Function of the game"
	totalNuts, gameMode = gameSetup()
	playAgain = "true"
	if(gameMode == 1):
		while(playAgain == "true"):
			playAgain = humanVsHumanGame(totalNuts)
	elif(gameMode == 2):
		pass
	else:
		pass

def humanVsHumanGame(totalNuts):
	"Runs a Human VS Human Game"
	remainingNuts = totalNuts
	player = 1
	while(remainingNuts > 0):
	#Runs one player at a time, then changes over to the next player when done
		print("There are {0} nuts on the board".format(remainingNuts))
		take = humanTurn(player) #Calls for a input for the player with 'player' being the number
		if(isLastNut(remainingNuts,take) == "true"):
			#Checks if the game is in a 'win' condition
			print("Player {0}, you lose.".format(player))
			playAgain = int(input("Play Again? (yes(1), no(0)) "))
			if (playAgain == 1):
				return("true") #Ends this functions call, removig it from the stack, then recalls to play again
			else:
				break #Breaks out as remaining code is not needed after a win and not wishing to play again
		remainingNuts = remainingNuts - take #Changing The value of how many nuts are let on the table
		if(player == 1): #Changes which player is getting called
			player = 2
		else:
			player = 1

def gameSetup():
	"Gets Called To set up game varibles, Starting Nuts and Game mode"
	print("Welcome to the game of nuts!")
	totalNuts = int( input("How many nuts are on the table to start? (10-100) "))
	while(totalNuts < 10 or totalNuts > 100):
		#Checks if the starting nuts is in the range
		totalNuts = int(input("Invaild Number (10-100) "))

	print("Game Modes: \n  Human VS Human (1)\n  Human VS AI (2)\n  Human VS Smart AI (3)")
	gameMode = int(input("Selcetion (1-3): "))
	while(gameMode < 1 or gameMode > 3):
		#Checks if the inputed gameMode is in the range
		gameMode = int(input("Invaild Selection (1-3): "))

	return(totalNuts,gameMode)

def isLastNut(remainingNuts,take):
	"Checks if the last player who toke a/some nut(s) grabbed the last one(s)"
	if (remainingNuts <= 3 and take == 3):
		#Test Case: If There is 3 or less nuts left and the player selects 3
		return("true")
	elif(remainingNuts <=2 and take >=2):
		#Test Case: If There is 2 or less nuts left and the Player selects 2 or more
		return("true")
	elif(remainingNuts == 1  and take >=1):
		#Test Case: If There is 1 nut left and the Player selects 1 or more
		return("true")
	else:
		#If all fail, then game isn't finished
		return("false")

def humanTurn(player):
	"Allows the human player to input thier selection"
	take = int(input("Player {0}: How many nuts do you take (1-3)? ".format(player)))
	while(take < 1 or take > 3):
		take = int(input("Invaild Number (1-3) "))
	return(take)

def aiSmartTurn():
	"Allows the Smart AI to make a selection"

def aiTurn():
	"Allows for the RNG AI to make a selection"

main()
