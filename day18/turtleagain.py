from turtle import Turtle, Screen
#import turtle as t
import random

tim= Turtle()
tim.shape("turtle")
screen= Screen()
colors=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]

def draw_shape(num_sides):
    angle= 360 /num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


'''
for drawing square
for i in range(4):
    tim.forward(100)
    tim.right(90)

for dashed line
for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
'''


screen.exitonclick()




