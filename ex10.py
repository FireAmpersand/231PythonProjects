class Point:

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __str__(self):
		return "({0}, {1})".format(self.x,self.y)

class Rectangle:
	"A rectangle class"

	def __init__(self, posn, w, h):
		"Create a new re3ctangle object"
		self.corner = posn
		self.width = w
		self.height = h

	def __str__ (self):
		return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

	def perimeter(self):
		return (self.height * 2) + (self.width *2)


	def flip(self):
		temp = self.height
		self.height = self.width
		self.width = temp

r = Rectangle(Point(0,0),10,5)
print(r.perimeter())
print("Height: " + str(r.height) + ", Width: " + str(r.width))
r.flip()
print("Height: " + str(r.height) + ", Width: " + str(r.width))
