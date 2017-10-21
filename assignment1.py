import turtle

#Inputing Values From The .dat File
xc,yc = eval(input())
r = eval(input())
x1,y1 = eval(input())
x2,y2 = eval(input())

#Turtle Object Creation And Setup
wn = turtle.Screen()
wn.setworldcoordinates(0,0,1000,1000)
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()
turtle1.speed(9)
turtle2.speed(9)
turtle3.speed(9)
turtle3.shape("blank")

def drawTurtles(lineTurtle,circleTurtle):
	"Draws The Turtles On The Screen"
	#Draws the circle, by moving to the (xc,yc - r) location
	circleTurtle.penup()
	circleTurtle.setx(xc)
	circleTurtle.sety(yc - r)
	circleTurtle.pendown()
	circleTurtle.circle(r)

	#Draws the line, moves to (x1,y1) and draws to (x2,y2)
	lineTurtle.penup()
	lineTurtle.setx(x1)
	lineTurtle.sety(y1 - 6)
	lineTurtle.pendown()
	lineTurtle.circle(6)
	lineTurtle.penup()
	lineTurtle.sety(y1)
	lineTurtle.pendown()
	lineTurtle.goto(x2,y2)
	lineTurtle.penup()
	lineTurtle.sety(y2 - 6)
	lineTurtle.pendown()
	lineTurtle.circle(6)

def solvingIntersections():
	"Calculating the intersections"
#Calculating the a,b,c
	a = ( (x2-x1) ** 2) + ( (y2-y1) ** 2)
	b = 2 * ( (x1-xc) * (x2-x1) + (y1-yc) * (y2-y1) )
	c = ( (x1-xc) ** 2) + ( (y1-yc) **  2) - (r**2)
	root = ( (b**2) - (4*a*c) )
#Testing if the root is negative
	if (root < 0 ):
		return(-20,-20,-20,-20)
	root = root ** (0.5)
#Making and testing the point on the line
	a1 = ( (b*-1) + root ) / ( 2 * a )
	a2 = ( (b*-1) - root ) / ( 2 * a )
	px1 = (1-a1) * x1 + (a1 *x2)
	py1 = (1-a1) * y1 + (a1*y2)
	px2 = (1-a2) * x1 + (a2 * x2)
	py2 = (1-a2) * y1 + (a2 * y2)
	if (px1 > x2 or  px1 < x1):
		px1 = -20
	if (px2 > x2 or px2 < x1):
		px2 = -20
#Returns the points (x,y) of the interestin(s)
	return(px1,py1,px2,py2)
def drawIntersections(intersectTurtle,point1x, point1y,point2x, point2y):
	"Draws The Instersection Circles"
	intersectTurtle.penup()
	intersectTurtle.goto(point1x,point1y - 6)
	intersectTurtle.pendown()
	intersectTurtle.circle(6)
	intersectTurtle.penup()
	intersectTurtle.goto(point2x,point2y-6)
	intersectTurtle.pendown()
	intersectTurtle.circle(6)

p1x,p1y,p2x,p2y = solvingIntersections()
drawTurtles(turtle1,turtle2)
drawIntersections(turtle3, p1x,p1y,p2x,p2y)
wn.mainloop()

