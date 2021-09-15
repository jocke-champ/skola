import turtle


def make_turtle(x, y, visible=True):
    t = turtle.Turtle()
    if not visible:
        t.hideturtle()
        t.speed(0)
    jump(t, x, y)
    return t


def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def rectangle(x, y, width, height, color, fill=False):
    t = make_turtle(x, y)
    t.hideturtle()
    t.fillcolor(color)
    if(fill):
        t.color(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()


def tricolore(x, y, h):
    w = h/2  	# färgfältens bredd
    rectangle(x, y, w, h, 'blue')
    rectangle(x+w, y, w, h, 'white')
    rectangle(x+2*w, y, w, h, 'red')


def pentagram(x, y, side, color, fill=False):
    t = make_turtle(x, y)
    t.hideturtle()
    t.fillcolor(color)
    t.setheading(270 - 36/2)
    t.begin_fill()
    if(fill):
        t.color(color)
        a = side * 1/2 * (3 - 5**(1/2))     # matematisk formel
        for i in range(5):
            t.forward(a)
            t.right(180-108)
            t.forward(a)
            t.left(180-36)
    else:   # skapar ihåligt pentagram
        for i in range(5):
            t.forward(side)
            t.left(180-36)
    t.end_fill()


def uppg_1(x, y, side, color):
    tricolore(x, y, (2 * side))
    for L in range(5):
        pentagram((x-side/2 + L*side), (y-side), side, color)
        pentagram((x-side/2 + L*side), (y+4*side), side, color)


def vietnamese_flag(x, y, height):
    width = 3/2 * height
    r = width/5
    sida = r * ((5+(5)**(1/2))/2)**(1/2)    # matematisk formel
    rectangle(x, y, width, height, 'red', fill=True)
    pentagram(x + width/2, y + height/2 + r, sida, 'yellow', fill=True)


# uppg 1
# uppg_1(0, 0, 100, "green")

# uppg 2
vietnamese_flag(-300, 0, 400)

turtle.done()
