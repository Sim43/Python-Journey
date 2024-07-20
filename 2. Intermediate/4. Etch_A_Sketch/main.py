from turtle import Turtle, Screen

timmy = Turtle()
timmy.speed('fastest')
timmy.pensize(3)

def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def turn_clockwise():
    timmy.right(10)


def turn_anticlockwise():
    timmy.left(10)


def cleari():
    timmy.clear()
    timmy.up()
    timmy.goto(0, 0)
    timmy.down()
    timmy.setheading(0)

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_anticlockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=cleari)
screen.exitonclick()
