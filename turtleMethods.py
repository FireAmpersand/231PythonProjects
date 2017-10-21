import turtle

wn = turtle.Screen()
alex = turtle.Turtle()


alex.write("Hello") #Alex writes Hello on the screen
alex.penup()
alex.goto(200,200)
alex.begin_fill()
alex.circle(20)
alex.end_fill()

wn.mainloop()
