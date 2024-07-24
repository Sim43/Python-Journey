from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput("Make your bet","Who will win the race? Enter a color:")
turtles = []
colors = ["red", "blue", "green", "black", "purple", "brown"]
y_pos = [-70, -40, -10, 20, 50, 80]
sc_end = 250
for i in range(len(colors)):
    tim = Turtle()
    tim.shape("turtle")
    color = colors[i]
    tim.color(color)
    tim.speed(2)
    tim.up()
    tim.goto(-sc_end + 20, y_pos[i])
    turtles.append(tim)


def rand_pace(turtle):
    pace = random.randint(0, 10)
    turtle.forward(pace)


y = 1
while y == 1:
    for i in range(len(colors)):
        rand_pace(turtles[i])
        if turtles[i].xcor() >= sc_end + 20:
            y = 0
            screen.bye()
            break
winner = colors[i]
if winner == guess:
    print("You win!")
else:
    print(f"You lose. The {winner} turtle was the winner.")
