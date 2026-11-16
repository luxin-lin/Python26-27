#main.py

from myfunctions import *
turtle.bgcolor("black")

bob.speed(0)

from random import randint


for times in range(200):
    x=randint(-600,600)
    y=randint(-600,600)
    jump(x,y)
    size=randint(1,1)
    bob.color("white")
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()


jump(0,0)
bob.color("white")

for times in range(200):
     bob.circle(times*2)
     bob.forward(times*2)
     bob.left(91)

bob.color("orange")
jump(0,0)
for times in range(200):
     bob.circle(times*2)
     bob.forward(times*2)
     bob.right(91)
