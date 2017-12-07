class Point:
	"Creates a point at x,y"
	def __init__(self, x=0, y=0):
		"Creates a new point at x,y"
		self.x = x
		self.y = y
	def distance_from_origin(self):
		"Computes the distance from the origin"
		return ((self.x **2) + (self.y**2)) **0.5
	def to_string(self):
		return"({0},{1})".format(self.x,self.y)
	def midpoint(self, p1, p2):
		mx = (p1.x + p2.x)/2
		my = (p1.y + p2.y)/2
		return Point(mx,my)
	def reflect_x(self):
		"Reflects the point over the xaxis"
		return "({0},{1})".format(self.x, -1 * self.y)

def distance(p1, p2):
	"Prints out the distance between two point"
	xdiff = (p2.x - p1.x)
	ydiff = (p2.y - p1.y)
	result = ((xdiff**2) + (ydiff **2))**0.5
	return result

def testSuite():
	p = Point(0,0)
	q = Point(3,5)
	print(distance(p,q))
	print(q.reflect_x())

testSuite()
