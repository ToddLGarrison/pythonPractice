from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("coral")

def draw_dash_line(x):
    for i in range(x):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.color("white")
        timmy_the_turtle.forward(10)
        timmy_the_turtle.color("coral")

def square_turtle(x,y):
    for i in range(x):
        draw_dash_line(y)
        timmy_the_turtle.left(90)

square_turtle(4,5)







screen = Screen()
screen.exitonclick()