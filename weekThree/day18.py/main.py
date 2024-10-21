import turtle as t
import random

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("coral")
timmy_the_turtle.speed("fastest")
timmy_the_turtle.pensize(5)
t.colormode(255)

# directions = [0, 90, 180, 270]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# def draw_dash_line(x):
#     for i in range(x):
#         timmy_the_turtle.forward(10)
#         timmy_the_turtle.penup()
#         timmy_the_turtle.forward(10)
#         timmy_the_turtle.pendown()

# def square_turtle(x,y):
#     for i in range(x):
#         draw_dash_line(y)
#         timmy_the_turtle.left(90)

# square_turtle(4,5)

# colors = ["CornflowerBlue", "DarkGreen", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)


# for shape_side in range(3, 11):
#     timmy_the_turtle.color(random.choice(colors))
#     draw_shapes(shape_side)

def random_walk(x):
    for i in range(x):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.forward(30)
        timmy_the_turtle.setheading(random.choice(directions))

random_walk(100)

screen = t.Screen()
screen.exitonclick()