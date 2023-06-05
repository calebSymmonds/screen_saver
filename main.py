from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape("arrow")
tim.color("red")
colormode(255)

while 1 > 0:
    start_x = -100
    start_y = 300
    tim.penup()
    tim.goto(start_x, start_y)
    tim.pendown()
    tim.speed("fastest")

    def random_color():
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        color = (red, green, blue)
        return color
    def draw_shape(num_sides):
        angle = 360 / num_sides
        for _ in range(num_sides):
            for _ in range(10):
                tim.forward(10)
                tim.penup()
                tim.forward(10)
                tim.pendown()
            tim.right(angle)

    for shape_side_n in range(3, 10):
        tim.color(random_color())
        draw_shape(shape_side_n)

    circle_start_x = 0
    circle_start_y = 0
    tim.penup()
    tim.goto(circle_start_x, circle_start_y)
    tim.pendown()

    def draw_spirograph(size_of_gap):
        for _ in range(int(360 / size_of_gap)):
            tim.color(random_color())
            tim.circle(100)
            tim.setheading(tim.heading() + size_of_gap)

    draw_spirograph(5)

    circle_start_x = -100
    circle_start_y = 100
    tim.penup()
    tim.goto(circle_start_x, circle_start_y)
    tim.pendown()

    draw_spirograph(5)

    circle_start_x = 100
    circle_start_y = 100
    tim.penup()
    tim.goto(circle_start_x, circle_start_y)
    tim.pendown()

    draw_spirograph(5)

    circle_start_x = -100
    circle_start_y = -100
    tim.penup()
    tim.goto(circle_start_x, circle_start_y)
    tim.pendown()

    draw_spirograph(5)

    circle_start_x = 100
    circle_start_y = -100
    tim.penup()
    tim.goto(circle_start_x, circle_start_y)
    tim.pendown()

    draw_spirograph(5)

screen = Screen()
