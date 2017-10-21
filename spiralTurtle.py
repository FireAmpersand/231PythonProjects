import turtle

wn = turtle.Screen()
wn.title("Spiral")
wn.bgcolor("Lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

tess.penup()
size = 20
for i in range(30):
	tess.stamp()
	size = size +3
	tess.forward(size)
	tess.right(24)

wn.mainloop()
