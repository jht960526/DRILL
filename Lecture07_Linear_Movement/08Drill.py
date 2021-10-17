import turtle
import random
import math


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     ' + str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())



def draw_circle(p1, p2):
    # draw_big_point(p1)
    # draw_big_point(p2)

    x1, y1 = p1
    x2, y2 = p2

    for i in range(0, 80):
        t = i / (2*math.pi)
        x = (50 - 100) * math.cos(t) + 100 * math.cos(t * (0.50 - 1))
        y = (50 - 100) * math.sin(t) - 100 * math.sin(t * (0.50 - 1))
        draw_point((x, y))

    draw_point(p2)

def draw_star(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    for i in range(0, 100):
        t = i / (2*math.pi)
        x = (10 - 25) * math.cos(t) + 25 * math.cos(t * (2.5 - 1))
        y = (10 - 25) * math.sin(t) - 25 * math.sin(t * (2.5 - 1))
        draw_point((x, y))


prepare_turtle_canvas()

p1 = 100, 20
p2 = 400, 500

draw_circle(p1, p2)
draw_star(p1, p2)
turtle.done()
