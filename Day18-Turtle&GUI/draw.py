class Draw:
    from turtle import Turtle

    def draw_shape(self,turtlename,sides,length1):
        turtlename=Turtle()
        turn = 360 / sides
        for _ in range(sides):
            turtlename.forward(length1)
            turtlename.right(turn)



