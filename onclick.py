from turtle import Screen, Turtle
from sys import exit
from libturtle import VolumeBar, StringToggler
import time

START_VOLUME_BAR = (-370, 250)
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
        # TODO(coco): update current drawing state text box
        t1.penup()
        toggler.toggle()
    else:
        # TODO(coco): update current drawing state text box
        t1.pendown()
        toggler.toggle()

def draw_color():
    s.tracer(False)
    x = -370
    pos = (x, 310)
    t3.penup()
    t3.goto(pos)
    t3.right(90)
    t3.pendown()
    t3.pensize(2)
    for color in colors:
        # determine colors
        if color == "white":
            t3.pencolor("black")
            t3.fillcolor("white")
        else:
            t3.color(color)

        # draw square
        t3.begin_fill()
        for _ in range(4):
            t3.fd(30)
            t3.left(90)

        # pen up, go to next square, pen down
        t3.end_fill()
        t3.penup()
        x += 40
        t3.goto(x, 310)
        t3.pendown()
    s.tracer(True)

def return_pos_click():
	s.onscreenclick(t3.goto)
	return t3.pos()

def change_color():
    color = colors.pop(0)
    t1.pencolor(color)
    colors.append(color)

def set_color():
    s.onkey(change_color, "space")
    s.listen()

def increase_pensize():
    pensize = t1.pensize() + PENSIZE_STEPSIZE
    if pensize <= MAX_PENSIZE:
        t1.pensize(pensize)
        v.fill_volume_bar(t1.pensize/MAX_PENSIZE)

def decrease_pensize():
    pensize = t1.pensize() - PENSIZE_STEPSIZE
    if pensize >= 1:
        t1.pensize(pensize)
        v.fill_volume_bar(t1.pensize/MAX_PENSIZE)

def set_pensize():
    s.onkey(increase_pensize, "Up")
    s.onkey(decrease_pensize, "Down")
    
def setup():
    t2.penup()
    t2.hideturtle()
    t3.hideturtle()
    t1.shape("turtle")
    t1.resizemode("auto")  # turtlesize increases with pensize
    s.screensize(600, 600)
    s.title("Paint, v0.0.1")

if __name__ == "__main__":
    t1 = Turtle() # main turtle
    t2 = Turtle() # runs hidden so that the program doesn't crash
    t3 = Turtle() # draws color bar
    s = Screen()
    v = VolumeBar(START_VOLUME_BAR, MAX_PENSIZE, s)
    toggler = StringToggler(START_PENUP, START_PENDOWN, "pen down", "pen up", s)
    colors = ["green", "yellow", "pink", "blue", "lightblue", "orange", "purple", "black", "white"]

    setup()
    draw_color()
    v.draw_volume_bar()
    v.fill_volume_bar(t1.pensize()/MAX_PENSIZE)
    return_pos_click()
    set_color()
    set_pensize()
    register_callbacks()
    s.mainloop()