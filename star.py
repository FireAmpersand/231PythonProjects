import turtle

wn = turtle.Screen()

star = turtle.Turtle()
star.pensize(5)
star.hideturtle()
star.left(36)

for i in range(5):
	star.forward(200)
	star.left(144)

wn.mainloop()
