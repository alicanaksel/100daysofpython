'''
HOW TO FIND THE COLORS IN A IMAGE
import colorgram

rgb_colors=[]
colors= colorgram.extract('image.jpg',30)
for color in colors:
    r= color.rgb.r
    g= color.rgb.g
    b= color.rgb.b
    new_color= (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
we found the color_list
'''
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim= turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list=[(235, 60, 98), (234, 215, 83), (130, 194, 207), (32, 172, 116), (212, 232, 237), (14, 123, 155), (243, 130, 97), (182, 51, 83), (229, 161, 181), (181, 135, 174), (0, 187, 225), (168, 213, 197), (234, 94, 71), (20, 60, 122), (36, 65, 86), (103, 196, 160), (139, 210, 224), (245, 162, 152), (98, 123, 165), (178, 191, 210)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count %10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=turtle_module.Screen()
screen.exitonclick()