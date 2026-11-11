# CMP 131 — Turtle Graphics Project 3
# Team name:
# Group members:
# Date:
# House name and theme:
#
# FILL IN THE BLANKS
# Replace EVERY ____ with a value, variable, or function name.
# For colors, replace ____ with a color name IN QUOTES.
# Example of a quoted color: "purple"
# This starter is intentionally incomplete. Fill the blanks before running.
# Keep the indentation. Read the assignment for sizes, angles, and positions.

import turtle


# Draw a filled square using the supplied size and color.
def draw_house(size, color):
    turtle.color(____)              # Which parameter holds the color?
    turtle.begin_fill()

    for side in range(____):       # How many sides does a square have?
        turtle.forward(____)       # Which parameter holds the side length?
        turtle.left(____)          # How far should a square turn?

    turtle.end_fill()


# Draw a filled triangle using the supplied size and color.
def draw_roof(size, color):
    turtle.color(____)
    turtle.begin_fill()

    for side in range(____):       # How many sides does a triangle have?
        turtle.forward(____)
        turtle.left(____)          # Use the outside turning angle.

    turtle.end_fill()


# STAGE 1 — Choose your team's colors.
wall_color = ____
roof_color = ____
turtle.bgcolor(____)
turtle.speed(3)

# STAGE 2 — Move to the bottom-left corner and draw the walls.
turtle.penup()
turtle.goto(____, ____)             # House starting position from the assignment.
turtle.setheading(0)
turtle.pendown()
draw_house(____, ____)              # Side length, then the wall color variable.

# STAGE 3 — Move to the top-left corner and draw the roof.
turtle.penup()
turtle.goto(____, ____)             # Roof starting position from the assignment.
turtle.setheading(0)
turtle.pendown()
draw_roof(____, ____)               # Matching side length, then roof color variable.

# STAGE 4 — Add one creative detail here.
# Choose a house name, sun, or door. Lift the pen before repositioning.
# Write your own commands below; do not add another function.


# Keep these final commands at the end.
turtle.hideturtle()
turtle.done()
