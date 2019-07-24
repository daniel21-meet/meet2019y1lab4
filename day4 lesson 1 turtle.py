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

import turtle
d = turtle.Turtle()
turtle.shape ('arrow')
d.shape ('circle')
turtle.bgcolor ('purple')
d.pencolor ('yellow')
d.pensize(2)
d.goto (0,100)
turtle.pensize (7)
turtle.pencolor ('green')
turtle.goto (0,-100)
turtle.goto (50,-100)
d.goto (-50,100)

turtle.mainloop
