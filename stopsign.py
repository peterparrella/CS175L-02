#CS175-02
#Peter Parrella
#turtlestopsign

import math
import turtle

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Compute some values
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

# Initialize turtle
turtle.speed(ANIMATION_SPEED)
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Draw outer red octagon
turtle.penup()
turtle.goto(-50, 125)
turtle.color("red")
turtle.begin_fill()
for _ in range(NUM_SIDES):
    turtle.forward(LENGTH)
    turtle.right(ANGLE)
turtle.end_fill()

# Draw inner white octagon
turtle.penup()
turtle.goto(-46, 117)
turtle.color("white")
turtle.begin_fill()
for _ in range(NUM_SIDES):
    turtle.forward(LENGTH - 11)
    turtle.right(ANGLE)
turtle.end_fill()

# Draw inner red octagon
turtle.penup()
turtle.goto(-44, 105)
turtle.color("red")
turtle.begin_fill()
for _ in range(NUM_SIDES):
    turtle.forward(LENGTH - 26)
    turtle.right(ANGLE)
turtle.end_fill()

# Draw "STOP" text
turtle.penup()
turtle.goto(0, -24)
turtle.color("white")
turtle.write("STOP", align="center", font=("Calabri", 35, "bold"))

turtle.done()
