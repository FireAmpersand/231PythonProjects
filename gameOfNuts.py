###################################
#	  Zachary Passmore	  #
#	      30043532		  #
#	      CPSC 231		  #
###################################

import random

def main():
	"The Main Function of the game"
	playAgain = 1
	oldAIHat = []
	while(playAgain == 1):
		totalNuts, gameMode = gameSetup()
		if(gameMode == 1):
			#Runs a Human Vs Human Game
			playAgain = humanVsHumanGame(totalNuts)
		elif(gameMode == 2):
			#Runs a Human Vs AI Game
			oldAIHat, playAgain = humanVsAIGame(totalNuts, oldAIHat)
		else:
			#Runs a Human Vs Trained Ai Game
			humanVsSmartAIGame(totalNuts)


def humanVsSmartAIGame(totalNuts):
	"Simulates 1000 games where the AI plays its self, then a human can challenge the AI"
	#Creating the hats that the AIs will need
	aiHatOne = aiHatBuilder(totalNuts,1)
	aiHatTwo = aiHatBuilder(totalNuts,1)
	print("Training AI, Please Wait")
	#Looping through 1000 games
	for i in range(1000):
		#Reseting variables every loop
		remainingNuts = totalNuts
		player = 1
		loss1 = "false"
		loss2 = "false"
		aiTakenHatOne = aiHatBuilder(totalNuts, 0)
		aiTakenHatTwo = aiHatBuilder(totalNuts, 0)
		while(remainingNuts > 0):
			#If the Ai playing is AI 1, then pass AI 1's hat to the ai method, else pass AI 2's hats
			if(player == 1):
				aiHatOne, aiTakenHatOne, loss1, remainingNuts = aiTurn(aiHatOne,aiTakenHatOne, remainingNuts,1)
			else:
				aiHatTwo, aiTakenHatTwo, loss2, remainingNuts = aiTurn(aiHatTwo,aiTakenHatTwo, remainingNuts, 1)

			#Checks if either AI has lost, if so the update the hats and break out of while loop
			if(loss1 == "true"):
				aiHatOne = aiChangeHatLose(aiHatOne, aiTakenHatOne)
				aiHatTwo = aiChangeHatWin(aiHatTwo, aiTakenHatTwo)
				break
			elif( loss2 == "true"):
				aiHatOne = aiChangeHatWin(aiHatOne, aiTakenHatOne)
				aiHatTwo = aiChangeHatLose(aiHatTwo, aiTakenHatTwo)
				break
			#Changing which AI is playing
			if (player == 1):
				player = 2
			else:
				player = 1
	#Combines The Best Values into one hat
	aiHat = combineAIHats(aiHatOne,aiHatTwo)
	print("Done")
	playAgain = 1
	#Loops through a humanVSAI Game
	while(playAgain == 1):
		aiHat, playAgain = humanVsAIGame(totalNuts,aiHat)


def humanVsAIGame(totalNuts,oldAIHat):
	"Runs a Human VS AI Game"
	remainingNuts = totalNuts
	aiHat = []
	aiTakenHat =[]
	#print(oldAIHat)
	if(len(oldAIHat) != totalNuts):
		#Checks if the old hat is the correct size
		aiHat = aiHatBuilder(totalNuts,1) #Creates a new ai hat with size totalNuts
		aiTakenHat = aiHatBuilder(totalNuts,0) #Creates a new secondary ai hat with size totalNuts
	else:
		aiHat = oldAIHat #Sets the current ai hat to the old version
		aiTakenHat = aiHatBuilder(totalNuts,0)	#Creates a new secondary ai hat with size totalNuts

	while(remainingNuts > 0):
		#Human's Turn
		playAgain, remainingNuts = humanTurn(1,remainingNuts)
		if(playAgain != -1):
		#Checks is the human lost, if so tell the ai to update its hat as a win
			return(aiChangeHatWin(aiHat,aiTakenHat), playAgain)
		#AI's Turn
		aiHat, aiTaken, playAgain, remainingNuts = aiTurn(aiHat,aiTakenHat,remainingNuts,0)
		if(playAgain != -1):
		#Checks if the ai lost, if so then update its hat as a loss
			return(aiChangeHatLose(aiHat,aiTakenHat),playAgain)


def humanVsHumanGame(totalNuts):
	"Runs a Human VS Human Game"
	player = 1
	remainingNuts = totalNuts
	while(remainingNuts > 0):
		#Runs one player at a time, then changes over to the next player when done
		playAgain, remainingNuts = humanTurn(player,remainingNuts) #Runs a players turn
		if(player == 1): #Changes which player is getting called
			player = 2
		else:
			player = 1

		if(playAgain != -1): #If playAgain is not in a play state (-1), end the function and pass playAgain up the call chain
			return(playAgain)


def gameSetup():
	"Gets Called To set up game varibles, Starting Nuts and Game mode. Returns starting nuts and gamemode"
	print("Welcome to the game of nuts!")
	totalNuts = int(input("How many nuts are on the table to start? (10-100) "))
	while(totalNuts < 10 or totalNuts > 100):
		#Checks if the starting nuts is in the range
		totalNuts = int(input("Invaild Number (10-100) "))
	print("Game Modes: \n  Human VS Human (1)\n  Human VS AI (2)\n  Human VS Smart AI (3)")
	gameMode = int(input("Selcetion (1-3): "))
	while(gameMode < 1 or gameMode > 3):
		#Checks if the inputed gameMode is in the range
		gameMode = int(input("Invaild Selection (1-3): "))
	return(totalNuts,gameMode)


def gameOverStatements(player):
	"Prints out which player lost and asks if they would like to play again. Return play again answer"
	playAgian = 1
	if (player == "AI"): #Checks if the player that lost is the AI, changes sentence structure if so
		print("AI Loses")
		return(int(input("Play again? (yes(1), no(0))"))) #Asks if the player would like to play agian
	else:
		print("Player {0}, you lose.".format(player))
		return(int(input("Play again? (yes(1), no(0))"))) #Asks if the player would like to play again


def isLastNut(remainingNuts,take):
	"Checks if the last player who toke a/some nut(s) grabbed the last one(s), returns true if is last nut(s)"
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


def humanTurn(player,remainingNuts):
	"Allows the human player to input thier selection, where player is the player number and remainingNuts is nuts left on table, returns play again and remaining nuts"
	print("There are {0} remaining nuts on the board".format(remainingNuts))
	take = int(input("Player {0}: How many nuts do you take (1-3)? ".format(player)))
	while(take < 1 or take > 3): #Check to make sure selection is vailid
		take = int(input("Invaild Number (1-3) "))
	if(isLastNut(remainingNuts,take) == "true"): #Checks if the last amount taken was the last nut(s)
		return(gameOverStatements(player),remainingNuts-take	) #Returns the playAgain choice and remaining Nuts
	else:
		return(-1,remainingNuts-take) #Returns a continue running statement with the updated remainingNuts


def aiTurn(aiHat, aiTakenHat, remainingNuts, playType):
	"Allows for the AI to make a selection"
	if(playType == 0): #Disables print statements when ais are playing
		print("There is {0} nuts left on the table".format(remainingNuts))
	move = aiChooseMove(aiHat[remainingNuts-1]) #Selects a move
	if(playType == 0): #Disables print statement when two ais are playing
		print("AI takes {0} nuts".format(move + 1))
	aiTakenHat[remainingNuts - 1] [move]  += 1 #Adds move to taken Hat
	if(isLastNut(remainingNuts, move + 1) == "true"):
		#If is last nut, runs the game over statements
		if(playType == 0):
			#If it is a humanVSAI Game it will ask to play Agian if the AI lost
			return(aiHat, aiTakenHat,gameOverStatements("AI"), remainingNuts - move + 1)
		else:
			#If it is a AI Vs AI game, then it just passes a lost value up the call chain
			return(aiHat, aiTakenHat, "true" , remainingNuts - move + 1)
	else:
		if(playType == 0):
			#If it is a Human Vs Ai game, it just passes a continue value up the call chain
			return(aiHat, aiTakenHat,-1, remainingNuts - (move + 1))
		else:
			#If it is a AI Vs AI Game, then it passes up a value saying this AI has not lost
			return(aiHat, aiTakenHat, "false", remainingNuts - (move + 1))


def aiHatBuilder(totalNuts, num):
	"Creates the AI's to hat, with internal numbers num"
	hat = [] 
	for i in range(totalNuts):
		#Loops in range totalNuts till each location has the proper numbers
		row = [num,num,num]
		hat += [row]
	return(hat)


def combineAIHats(aiHatOne, aiHatTwo):
	"Takes the two hats generated from two AIs playing against each other and combines it into one hat"
	aiHat = []
	#The outer loop for comparing values
	for i in range(len(aiHatOne)):
		aiTemp = [1,1,1] #Temp list for storing values
		for a in range(3): #Inner loop, checcks if one value is larger than the other
			if(aiHatOne[i][a] > aiHatTwo[i][a]):
				aiTemp[a] = aiHatOne[i][a] #Sets the value to hat one's value 
			elif(aiHatOne[i][a] < aiHatTwo[i][a]):
				aiTemp[a] = aiHatTwo[i][a] #Sets the value to hat Two's value
		aiHat = aiHat + [aiTemp]
	#print(aiHat)
	return(aiHat) #Returns the new hat


def aiChooseMove(aiHat):
	"Chooses a move based on the AI's Hat"
	total = aiHat[0] + aiHat[1] + aiHat[2]
	rInt = random.randint(1,total)
	if (rInt <= aiHat[0]):
		# Move 0 is equal to taking 1 nut
		move = 0
	elif (rInt <= aiHat[0] + aiHat[1]):
		#Move 1 is equal to taking 2 nuts
		move = 1
	else:
		#Move 2 is equal to taking 3 nuts
		move = 2
	return(move)


def aiChangeHatWin(aiHat, aiTakenHat):
	"Updates the AI's hat to add in the values in the secondary hat"
	for i in range(len(aiHat)):
		#Looping through the outer loop
		for a in range(3):
			#Looping through the inner loop
			aiHat[i][a] = aiHat[i][a] + aiTakenHat[i][a]
	#print(aiHat)
	return(aiHat)


def aiChangeHatLose(aiHat, aiTakenHat):
	"Updates the AI's hat to subtract the values in the secondary"
	for i in range(len(aiHat)):
		#Looping through outer loop
		for a in range(3):
			#Looping through inner loop
			if(aiHat[i][a] != 1):
				#Making sure that each sets has at least one number
				aiHat[i][a] = aiHat[i][a] - aiTakenHat[i][a]
	#print(aiHat)
	return(aiHat)


main()
