from turtle import Turtle, Screen
import random
import colorgram


def rgb_colors_list(image_name, num_of_col):
    colors = colorgram.extract(image_name, num_of_col)
    color_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_1 = (r, g, b)
        color_list.append(rgb_1)
    return color_list


tim = Turtle()
tim.hideturtle()
tim.penup()
tim.setx(-250)
tim.sety(-250)
tim.pendown()

my_screen = Screen()
my_screen.colormode(255)


def draw(space, x):
    color_rgb = rgb_colors_list("images (19).jpeg", 10)
    for i in range(x):
        for j in range(x):

            tim.dot(20, random.choice(color_rgb))

            tim.forward(space)
        tim.backward(space * x)

        tim.left(90)
        tim.forward(space)
        tim.right(90)


tim.penup()
draw(50, 10)


my_screen.exitonclick()