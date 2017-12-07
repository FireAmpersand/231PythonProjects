def main():
	strn = input("Enter text: ").lower()
	letterCount = {}
	for letter in strn:
		letterCount[letter] = letterCount.get(letter, 0) + 1
		if letter == " ":
			del(letterCount[letter])
	letterItems = list(letterCount.items())
	letterItems.sort()
	print(letterItems)
	for i in range(len(letterItems)):
		tup = letterItems[i]
		valueOne = tup[0]
		valueTwo = tup[1]
		print(valueOne + " : " +  str(valueTwo))

main()
