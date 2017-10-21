def mirror(text):
	length = len(text)
	while (length > 0):
		text = text + text[length-1]
		length = length -1
	return(text)

def remove_letter(letter, text):
	length = len(text)
	newText = ""
	for i in range(length):
		if (text[i] != letter):
			newText = newText + text[i]
	return(newText)

def testSuite():
	print(mirror("good"))
	print(mirror("Python"))
	print(mirror(""))
	print(mirror("a"))

	print(remove_letter("a","apple"))
	print(remove_letter("a","banana"))
	print(remove_letter("z","banana"))
	print(remove_letter("i","Mississippi"))
	print(remove_letter("b",""))
	print(remove_letter("b","c"))

testSuite()
