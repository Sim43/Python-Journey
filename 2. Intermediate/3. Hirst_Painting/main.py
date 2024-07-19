import turtle
from turtle import Turtle, Screen
import random
# colors extracted using colorgram
colors_list = [(246, 244, 243), (235, 239, 246), (241, 246, 243), (247, 239, 242), (135, 164, 199), (223, 151, 105),
               (31, 44, 63),
               (200, 137, 148), (160, 61, 51), (235, 212, 93), (49, 100, 139), (138, 181, 162), (147, 64, 72),
               (56, 49, 47), (161, 32, 30),
               (62, 115, 100), (228, 165, 171), (51, 40, 43), (169, 29, 33), (210, 86, 76), (236, 167, 156),
               (34, 60, 54), (16, 95, 70),
               (34, 60, 105), (171, 188, 219), (191, 101, 109), (109, 127, 155), (174, 200, 191), (36, 149, 206),
               (20, 83, 104)]

turtle.colormode(255)
timmy = Turtle()


def paint(height, width):
    start = -180
    timmy.up()
    timmy.goto(start, start)
    timmy.down()
    for i in range(height):
        for _ in range(width):
            timmy.dot(20, random.choice(colors_list))
            timmy.up()
            timmy.forward(50)
            timmy.down()
        timmy.up()
        timmy.goto(start, start + (i + 1) * 50)
        timmy.down()

paint(10, 10)
screen = Screen()
screen.exitonclick()
