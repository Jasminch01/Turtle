
# #love with turtle
from turtle import*
color("red")
begin_fill()
left(50)
forward(100)
circle(40, 180)
left(260)
circle(40, 180)
forward(100)
end_fill()
exitonclick()
# draw a ractangle with turtle
import turtle;
turtle.shape("turtle")
turtle.speed(1)
turtle.color("blue")
turtle.begin_fill()
for i in range(8): #for loop
    turtle.forward(200)
    turtle.left(90)
turtle.end_fill()
turtle.done()

# Turtle wheel

import turtle;

turtle.color("red")
turtle.speed(5)
counter = 0
while counter < 36:
    for i in range (4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    counter += 1
turtle.exitonclick()
