import turtle
wn = turtle.Screen()
wn.title("Hello, Zach")
wn.bgcolor(input("Enter BackGround Color: "))
zach = turtle.Turtle()
zach.color(input("Enter Turtle Color: "))
zach.pensize(int(input("Enter The Pen Size: ")))

zach.forward(50)
zach.left(120)
zach.forward(50)

wn.mainloop()
