import turtle

def create_square(t,sz):
	"Makes a square with turtle t, with size sz"
	t.forward(sz)
	t.left(90)
	t.forward(sz)
	t.left(90)
	t.forward(sz)
	t.left(90)
	t.forward(sz)
	t.left(90)

def move_outward(t):
	"Moves the turtle to the next sqaure location"
	t.penup()
	t.right(90)
	t.forward(10)
	t.right(90)
	t.forward(10)
	t.right(180)
	t.pendown()

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tur = turtle.Turtle()
tur.color("hotpink")
tur.pensize(3)

size = 20

for i in range(5):
	create_square(tur,size)
	size = size + 20
	move_outward(tur)

wn.mainloop()
