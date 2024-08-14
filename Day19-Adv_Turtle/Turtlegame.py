from turtle import Turtle, Screen


scr = Screen()


Ryan = Turtle()

scr.colormode(255)

def Move():
    Ryan.forward(10)

def Move_Back():
    Ryan.backward(10)

def Move_Rt():
    Ryan.right(10)
    
    
def Move_Lt():
    Ryan.left(10)

def Clr():
    Ryan.clear()
    Ryan.penup()
    Ryan.home()
    Ryan.pendown()

scr.listen()

scr.onkey(key="w", fun=Move)
scr.onkey(key="s", fun=Move_Back)
scr.onkey(key="a", fun=Move_Lt)
scr.onkey(key="d", fun=Move_Rt)
scr.onkey(key="c", fun=Clr)
scr.exitonclick()