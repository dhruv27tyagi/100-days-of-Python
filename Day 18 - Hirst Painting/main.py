from turtle import Screen
import turtle as turtle_module
import colorgram
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

#colors = colorgram.extract('Day 18 - Hirst Painting\pic.jpg',30)

#rgb_colors=[]

#for color in colors:
 #   r = color.rgb.r
  #  g = color.rgb.g
   # b = color.rgb.b
    #new_color = (r,g,b)
    #rgb_colors.append(new_color)
    

#print(rgb_colors)

color_list =[(233, 233, 232), (231, 233, 237), (236, 232, 234), (222, 232, 225), (208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (221, 206, 107), (132, 177, 203), (45, 55, 104), (158, 46, 83), (168, 160, 39), (129, 189, 143), (84, 20, 44), (38, 42, 66), (187, 93, 106), (187, 139, 169), (85, 123, 181), (59, 39, 31), (88, 157, 91), (79, 153, 165), (194, 79, 72), (45, 74, 77), (161, 201, 220), (80, 73, 44), (58, 131, 122), (217, 176, 187), (220, 182, 167), (166, 207, 164)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()