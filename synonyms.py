
'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 18, 2015.
'''
import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
	"Returns the cosine similarity between two dictionaries"
	#Creating the master variable
	cosineValue = 0
	#Creating Variables for easy calling to dictionary values
	vectorOneValues = list(vec1.values())
	vectorTwoValues = list(vec2.values())
	#Looping through each key in the dictionary
	for k in vec1:
		#Try/ Except here in case a key is not in a dictionary
		try:
			#Getting the top values based on the current key: k
			top = (vec1[k]) * (vec2[k])
			#Creating two bottom variable to store their math before multiplying them together later
			bottomOne = 0
			bottomTwo = 0
			#Looping through all the values in each dictionary
			for i in range(len(vec1)):
				#Adding the square of a value to the vector's bottom variable
				bottomOne += vectorOneValues[i] ** 2
				bottomTwo += vectorTwoValues[i] ** 2
			#Multipling the bottom values together, then taking the sqaure root
			bottom = (bottomOne * bottomTwo) ** 0.5
			#Setting the master variable to the result of top divided by the bottom
			cosineValue += (top/bottom)

		except:
			#If the try fails, then its just going to reloop with a new key
			pass
	#Returning the result
	return(cosineValue)

def build_semantic_descriptors(sentences):
	"Creates a semantic descriptors dictionary from a list of sentences"
	#The master dictionary containing the semantic descriptors
	master = {}
	#print(sentences)
	#Looping through each sentence list
	for currSen in range(len(sentences)):
		#Looping through each word in the current sentence 
		for currWord in sentences[currSen]:
			#If the current word hasn't had a 'mini' dictionary created, then build one
			if currWord not in master:
				#print("running : {0}".format(currWord))
				master[currWord] = build_smaller_dictionary(sentences, currWord)
	#Return the master dictionary
	return(master)

def build_smaller_dictionary(sentences, targetWord):
	"Builds and returns The smaller dictionary for the given word"
	#Smaller Dictionary Variable
	dict = {}
	#Looping through each sentence in the list
	for sen in range(len(sentences)):
		#Checking if the target word is in the selected sentence, if not move on to next sentence
		if targetWord in sentences[sen]:
			#Looping through all words in the current sentence
			for i in range(len(sentences[sen])):
				#Checking that it doesn't add itself to the dictionary
				if sentences[sen][i] !=  targetWord:
					#If the current word is in the dictionary, add 1
					if sentences[sen][i] in dict:
						dict[sentences[sen][i]] += 1
					#If the current word isn't in the dictionary, set it to 1
					else:
						dict[sentences[sen][i]] = 1
	#Return the smaller dictionary
	return dict


def build_semantic_descriptors_from_files(filenames):
	"Imports the text from the files provided, returns the semantic descriptors"
	#Master text variable
	text = ""
	#Looping through all the files
	for i in range(len(filenames)):
		#Setting the current file
		file = open(filenames[i], "r", encoding="utf-8")
		#Looping indefinalty untill there is nothing left in the file
		while(1==1):
			#Getting the current line
			currentLine = file.readline()
			#If the line has nothing, break out
			if len(currentLine) == 0:
				break
			#Adding the currentLine to the master text 
			text += currentLine
	#Changing to lower case, and then removing other puncuation
	text = text.lower()
	text = text.replace(",", "")
	text = text.replace("-", "")
	text = text.replace("--","")
	text = text.replace(":","")
	text = text.replace(";","")
	text = text.replace('"','')
	text = text.replace("'", "")
	text = text.replace("?",".")
	text = text.replace("!",".")
	text = text.replace("(", "")
	text = text.replace(")", "")
	#Splitting the text by either '.' , '?' or '!'
	tempSentences = text.split(".")
	#Master sentence variable
	sentences = []
	#Looping through the previous split to format properly
	for i in range(len(tempSentences)):
		#Making sure to remove a newline character
		if len(tempSentences[i]) != 1:
			#Adding to the master sentence
			sentences.append(tempSentences[i].split())

	return(build_semantic_descriptors(sentences))


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass


#build_semantic_descriptors_from_files(["underground.txt"])
des = build_semantic_descriptors_from_files(["pg7178.txt"])
#most_similar_word(
