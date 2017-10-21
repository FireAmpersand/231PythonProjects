import turtle

def draw_multicolor_square(t,sz):
	"Makes turtle t, draw a square with size sz. The sides also change color"
	for i in ["red","purple","hotpink","blue"]:
		t.color(i)
		t.forward(sz)
		t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)
tess.speed(8)

size = 20
for i in  range(10000):
	draw_multicolor_square(tess, size)
	size = size + 10
	tess.forward(10)
	tess.right(18)

wn.mainloop()
