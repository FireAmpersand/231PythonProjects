import turtle

wn = turtle.Screen()

alex = turtle.Turtle()

alex.penup() #lifts the pen
alex.forward(50)
alex.pendown() #puts the pen down
alex.forward(80)
alex.left(90)

alex.shape("turtle") #changes the shape, arrow, blank,circle,classic,square,triangle,turtle
alex.speed(10) #speed turtle, 1-10
alex.forward(70)

wn.mainloop()
