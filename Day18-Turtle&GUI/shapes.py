from turtle import Turtle, Screen
import random

x = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]



class Draw:
    def draw_shape(self, turtlename, sides, length1):
        turn = 360 / sides
        turtlename.color(random.choice(x))
        for _ in range(sides):
            turtlename.forward(length1)
            turtlename.right(turn)

    def draw_walk(self,walks):
        for _ in range(walks):
            tia.color(random.choice(x))
            tia.forward(50)
            tia.right(random.randint(0,360))

# Create a Screen object
screen = Screen()

# Create a Turtle object
tia = Turtle()
tia.shape("turtle")
tia.color("green")


# Create an instance of the Draw class
drawer = Draw()

# Call the draw_shape method on the instance
#for _ in range(random.randint(10,10)):
    #drawer.draw_shape(tia, random.randint(5,15), 100)
#screen.clearscreen()
drawer.draw_walk(random.randint(10,50))

# Close the screen on click
screen.exitonclick()
