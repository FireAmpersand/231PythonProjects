import turtle
def drawTurtles(t, height):
	"Get turtle t to draw one bar, of height"
	t.begin_fill()
	t.left(90)
	t.forward(height)
	t.write(" " + str(height))
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(height)
	t.end_fill()
	t.left(90)
	t.forward(10)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("blue" , "red")
alex.pensize(3)
xs = [48,117,200,240,160,260,220]
for v in xs:
	drawTurtles(alex, v)
wn.mainloop()
