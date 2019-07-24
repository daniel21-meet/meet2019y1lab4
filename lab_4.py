"""
import turtle
turtle.shape ('turtle')
d = turtle.clone ()
d.shape ('square')
d.goto (100,100)
d.penup ()
d.goto (0,0)
d.pendown ()
d.goto (100,0)
d.goto (100,100)
d.goto (0,100)
d.goto (0,0)
c = turtle.Turtle ()
c.shape ('triangle')
c.goto (50,100)
c.goto (100,0)
c.goto (0,0)
d.goto (300,300)
d.stamp ()
d.goto(100,100)
turtle.stamp ()
turtle.goto (0,300)
turtle.clearstamps ()


turtle.mainloop
"""
"""
import turtle
d = turtle.Turtle()
d.color ('white')
turtle.left (90)
turtle.color ('blue')
turtle.shape ('arrow')
d.shape ('circle')
turtle.bgcolor ('purple')
d.pencolor ('yellow')
d.pensize(3)
d.goto (0,100)
turtle.pensize (6)
turtle.pencolor ('green')
turtle.goto (0,-100)
turtle.goto (50,-100)
d.goto (-50,100)             
d.pencolor ('white')
d.goto (-50,0)
turtle.pencolor ('blue')
turtle.goto(50,0)
"""

import turtle

def up():
    turtle.forward (50)
def down():
    turtle.back (50)
def left():
    turtle.left(45)
def right():
    turtle.right (45)
turtle.onkeypress(up, "w")
turtle.onkeypress(down, "s")
turtle.onkeypress(left, "a")
turtle.onkeypress(right, "d")
turtle.listen ()

turtle.mainloop
