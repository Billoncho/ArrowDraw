# ArrowDraw.py
# Billy Ridgeway
# Creates a program to draw using the arrow keys.

import turtle                   # Imports the turtle library.
t = turtle.Pen()                # Creates a pen named t.
t.speed(0)                      # Sets the pen's speed to fast.
t.turtlesize(2,2,2)             # Sets the size of the pen.
def up():               # Defines the function for moving the pen forward.
    t.forward(50)
def left():             # Defines the function for turning the pen to the left.
    t.left(90)
def right():            # Defines the function for turning the pen to the right.
    t.right(90)
turtle.onkeypress(up, "Up")         # Calls the up function.
turtle.onkeypress(left, "Left")     # Calls the left function.
turtle.onkeypress(right, "Right")   # Calls the right function.
turtle.listen()                     # Listens for keyboard events.
