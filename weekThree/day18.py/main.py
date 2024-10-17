from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("coral")

def square_turtle(x):
    for i in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(90)

square_turtle(4)







screen = Screen()
screen.exitonclick()