def replace(s , old , new):
	"Replaces the old letter with the new one"

	word = s.split(old)
	newWord = new.join(word)

	print(newWord + "\n")
	return(newWord)


def testSuite():
	print("Mississippi","i","I")
	replace("Mississippi","i","I")
	s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
	print(s,"om", "am")
	s = replace(s, "om", "am")
	print(s, "o","a")
	replace(s,"o","a")

testSuite()
