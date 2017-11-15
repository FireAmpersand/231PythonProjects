def testSuite():
	print(flatten([2,9,[2,1,13,2],8,[2,6]],[]))
	print(flatten([[9,[7,1,13,2],8],[7,6]],[]))
	print(flatten([[9,[7,1,13,2],8],[2,6]],[]))
	print(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]],[]))
	print(flatten([],[]))


def flatten(list,newList):
	for element in list:
		if type(element) == type([]):
			newList = flatten(element,newList)
		else:
			newList.append(element)
	return newList


testSuite()
