'''import turtle as t
import random

neil = t.Turtle()

x = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

t.colormode(255)

def randomcolor():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    randomcolor = (r, g, b)
    return randomcolor

for _ in range(100):
    neil.pensize(random.randint(1, 10))
    neil.speed(random.randint(1, 10))
    neil.color(randomcolor())
    neil.forward(30)
    neil.setheading(random.randint(0, 360))
'''

import turtle as t
import random

# Initialize the turtle and screen settings
t.colormode(255)  # Set color mode to 255 to use RGB values
neil = t.Turtle()

neil.speed('fastest')  # Set the turtle speed to the fastest

def randomcolor():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    randomcolor = (r, g, b)
    return randomcolor

def draw_circle(sizeofgap):
    for _ in range(int(360 / sizeofgap)):
        neil.color(randomcolor())
        neil.circle(100)
        neil.setheading(neil.heading() + sizeofgap)

draw_circle(5)

# Create the screen object and set exit on click
screen = t.Screen()
screen.exitonclick()
