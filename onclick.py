from sys import exit
from turtle import Screen, Turtle

from libturtle import StringToggler, VolumeBar

START_VOLUME_BAR = (80, 280)
START_PENUP = (0, 300)
START_PENDOWN = (0, 280)
MAX_PENSIZE = 21
PENSIZE_STEPSIZE = 2


def register_callbacks():
    t1.onclick(t1.goto, 1)
    s.onscreenclick(t1.goto, 1)
    t1.onclick(pen_change, 3)
    s.onkey(screen_exit_handler, "Escape")


def screen_exit_handler():
    print("[debug] got ESC, quitting")
    exit(0)


def pen_change(xdummy, ydummy):
    global toggler

    if t1.isdown():
        t1.penup()
        toggler.toggle()
    else:
        t1.pendown()
        toggler.toggle()


def draw_color():
    s.tracer(False)
    x = -370
    pos = (x, 310)
    t2.penup()
    t3.penup()
    t2.goto(pos)
    t3.goto(pos)
    t2.right(90)
    t3.right(90)
    t2.pendown()
    t3.pendown()
    t2.pensize(1)
    t3.pensize(5)
    for _ in range(4):
        t3.fd(30)
        t3.left(90)
    for color in colors:
        # determine colors
        if color == "white":
            t2.pencolor("black")
            t2.fillcolor("white")
        else:
            t2.color(color)

        # draw square
        t2.begin_fill()
        for _ in range(4):
            t2.fd(30)
            t2.left(90)

        # pen up, go to next square, pen down
        t2.end_fill()
        t2.penup()
        x += 40
        t2.goto(x, 310)
        t2.pendown()
    s.tracer(True)



def return_pos_click():
    s.onscreenclick(t2.goto)
    return t2.pos()


def change_color():
    color = colors.pop(0)
    t1.pencolor(color)
    colors.append(color)
    t3.pensize(3)
    s.tracer(False)
    if color == "black":
        t3.pencolor("dim gray")
    else:
        t3.pencolor("black")
    t3.penup()
    t3.goto

    s.tracer(True)


def set_color():
    s.onkey(change_color, "space")
    s.listen()


def increase_pensize():
    pensize = t1.pensize() + PENSIZE_STEPSIZE
    if pensize <= MAX_PENSIZE:
        t1.pensize(pensize)
        v.fill_volume_bar(t1.pensize()/MAX_PENSIZE)


def decrease_pensize():
    pensize = t1.pensize() - PENSIZE_STEPSIZE
    if pensize >= 1:
        t1.pensize(pensize)
        v.fill_volume_bar(t1.pensize()/MAX_PENSIZE)


def set_pensize():
    s.onkey(increase_pensize, "Up")
    s.onkey(decrease_pensize, "Down")


def setup():
    t2.hideturtle()
    t3.hideturtle()
    t1.shape("turtle")
    t1.resizemode("auto")  # turtlesize increases with pensize
    s.screensize(600, 600)
    s.title("Paint, v0.0.1")


if __name__ == "__main__":
    t1 = Turtle()  # main turtle
    t2 = Turtle()  # draws color bar
    t3 = Turtle()  # selects current color
    s = Screen()
    v = VolumeBar(START_VOLUME_BAR, MAX_PENSIZE, s)
    toggler = StringToggler(START_PENUP, START_PENDOWN,
                            "pen down", "pen up", s)
    colors = ["green", "yellow", "pink", "blue",
              "lightblue", "orange", "purple", "black", "white"]

    setup()
    draw_color()
    v.draw_volume_bar()
    v.fill_volume_bar(t1.pensize()/MAX_PENSIZE)
    return_pos_click()
    set_color()
    set_pensize()
    register_callbacks()
    s.mainloop()
