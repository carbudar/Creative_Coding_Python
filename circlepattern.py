from turtle import *

# Set up the screen size
canvassize = 600
setup(canvassize, canvassize)
title("Circle Grid Sketch")
speed(0)
bgcolor('black')
color('white')
pensize(0.7)

# Define grid properties
rows = cols = 10  # Number of rows and columns

circle_radius = canvassize / rows
circle_radius_small = 10

horizontal_spacing = circle_radius * 2  # Halfway to the previous circle
vertical_spacing = circle_radius  # Touching but not overlapping

# Move turtle to the top-left starting position
penup()
start_x = -((cols - 1) * horizontal_spacing) / 2
start_y = ((rows - 1) * vertical_spacing) / 2

# Draw the grid of circles
for i in range(rows):
    row_offset = (circle_radius) if i % 2 == 1 else 0  # Indent odd rows
    for j in range(cols):
        x = start_x + j * horizontal_spacing + row_offset
        y = start_y - i * vertical_spacing
        goto(x, y - circle_radius)  # Adjust for correct circle placement
        pendown()
        circle(circle_radius)
        penup()

         # Draw inner circle with white fill
        fillcolor('white')
        begin_fill()
        goto(x, y - circle_radius_small)
        pendown()
        circle(circle_radius_small)
        end_fill()
        penup()


hideturtle()
mainloop()
