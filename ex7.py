def flatten(list, newList):
	for i in range(len(list)):
		if type(list[i]) is  type([]):
			newList = flatten(list[i], newList)
		else:
			newList.append(list[i])
	return(newList)

def testSuite():
	print(flatten([2,9,[2,1,13,2],8,[2,6]], []))
	print(flatten([[9,[7,1,13,2],8],[7,6]], []))
	print(flatten([[9,[7,1,13,2],8],[2,6]], []))
	print(flatten([['this',['a',['thing'],'a'],'is'],['a','easy']], []))

testSuite()
