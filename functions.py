import turtle

def draw_square(t,sz):
	"Draws a square with Turtle t with size sz"
	for i in range(4):
		t.forward(sz)
		t.left(90)

wn = turtle.Screen()
alex = turtle.Turtle()
draw_square(alex,50)
wn.mainloop()
