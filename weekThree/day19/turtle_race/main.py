from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win the race?: ")
print(user_bet)

tim = Turtle()

screen.exitonclick()