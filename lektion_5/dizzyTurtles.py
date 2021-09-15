import turtle
import random


def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def rectangle(x, y, width, height, color):
    t = turtle.Turtle()
    jump(t, x, y)
    t.hideturtle()
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()


def move_random(t):
    ny_kurs = random.randint(-45, 45) + t.heading()
    ny_stracka = random.randint(0, 25)
    if (abs(t.xcor()) > 250) or (abs(t.ycor()) > 250):  # rektangelns yta
        t.setheading(t.towards(0, 0))
    else:
        t.setheading(ny_kurs)
    t.forward(ny_stracka)


t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.color('steelblue')
t2.color('tomato')
close_ggr = 0

rectangle(-250, -250, 500, 500, 'plum')
jump(t1, random.randint(-250, 250), random.randint(-250, 250))
jump(t2, random.randint(-250, 250), random.randint(-250, 250))
for i in range(250):
    move_random(t1)
    move_random(t2)
    if t1.distance(t2) < 50:    # inbyggt metod
        t1.write('close')
        close_ggr = close_ggr + 1

print(close_ggr, ' gånger nära varandra')
turtle.done()
