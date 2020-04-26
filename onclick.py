from turtle import Screen, Turtle
import time

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
s1 = Screen()
s1.screensize(600, 600)
t1.resizemode("auto")

MAX_PENSIZE = 18
PENSIZE_STEPSIZE = 2
colors = ["green", "yellow", "pink", "blue", "lightblue", "orange", "purple", "black", "white"]
    
def register_callbacks():
    t1.onclick(t1.goto, 1)
    s1.onscreenclick(t1.goto, 1)
    t1.onclick(pen_change, 3)

def pen_change(xdummy, ydummy):
    if t1.isdown():
        # write new state
        t1.penup()
    else:
        # write new state
        t1.pendown()

def draw_color():
    t3.speed(30)
    x = -370
    pos = (x, 310)
    t3.penup()
    t3.goto(pos)
    t3.right(90)
    t3.pendown()
    for color in colors:
        if color == "white":
            t3.pencolor("black")
        else:
            t3.pencolor(color)
        t3.fillcolor(color)
        t3.begin_fill()
        for _ in range(4):
            t3.fd(30)
            t3.left(90)
        t3.end_fill()
        t3.penup()
        x += 40
        t3.goto(x, 310)

def return_pos_click():
	s1.onscreenclick(t3.goto)
	print(t3.pos())
	return t3.pos()

def change_color():
    color = colors.pop(0)
    t1.pencolor(color)
    colors.append(color)

def set_color():
    s1.onkey(change_color, "space")
    s1.listen()

def increase_pensize():
    pensize = t1.pensize() + PENSIZE_STEPSIZE
    if pensize < MAX_PENSIZE:
        t1.pensize(pensize)

def decrease_pensize():
    pensize = t1.pensize() - PENSIZE_STEPSIZE
    if pensize >= 1:
        t1.pensize(pensize)

def set_pensize():
    s1.onkey(increase_pensize, "Up")
    s1.onkey(decrease_pensize, "Down")
    

if __name__ == "__main__":
    s1.title("Paint, v0.0.1")
    draw_color()
    return_pos_click()
    set_color()
    set_pensize()
    t2.penup()
    t2.hideturtle()
    t3.hideturtle()
    t1.shape("turtle")
    t1.resizemode("user")  # TODO(coco): what is this, exactly?
    register_callbacks()
    x = 1
    y = x

    while True:
        t2.forward(1)