import turtle
color1 = input("Enter color 1: ")
color2 = input("Enter color 2: ")
color3 = input("Enter color 3: ")
color4 = input("Enter color 4: ")

colors = [color1, color2, color3, color4]

wn = turtle.Screen()

alex = turtle.Turtle()

for c in colors:
	alex.color(c)
	alex.forward(80)
	alex.left(90)

wn.mainloop()
