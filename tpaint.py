import os
import subprocess
from tkinter import Label, messagebox, Entry, Tk
import platform
from sys import exit
from turtle import RawTurtle, Screen, Turtle, mainloop

from libturtle import StringToggler, VolumeBar



settings = {
    "start_volume_bar": (80, 280),
    "start_penup": (0, 300),
    "start_pendown": (0, 280),
    "max_pensize": 21,
    "pensize_stepsize": 2,
    "title": "Turtle Paint v0.0.2",
    "screen_dims": (800, 600),
}

class TurtlePaint():
    def __init__(self, settings):
        self.t1 = Turtle() # main turtle
        self.t2 = Turtle() # draws color bar
        self.t3 = Turtle() # selects current color
        self.t4 = Turtle() # draws tool bar border
        self.t5 = Turtle() # makes shape stamps
        self.t6 = Turtle() # selects current shape
        self.t7 = Turtle() # refers to instructions
        self.t8 = Turtle() # selects current fillcolor
        self.s = Screen()
        self.instructions = {
                               "b": "begin filling",
                               "c": "clear all",
                               "e": "end filling",
                               "f": "change fillcolor",
                               "h": "turn left",
                               "j": "go backward",
                               "k": "go forward",
                               "l": "turn right",
                               "p": "pen up / pen down",
                               "s": "save picture",
                               "t": "change turtle shape",
                               "u": "undo last drawing",
                               "space": "change pencolor",
                               "arrow_up": "increase pensize",
                               "arrow_down": "decrease pensize"
        }
        self.v = VolumeBar(settings.get("start_volume_bar"),
                           settings.get("max_pensize"), self.s)
        self.toggler = StringToggler(settings.get("start_penup"),
                                     settings.get("start_pendown"),
                                     "pen down", "pen up", self.s)
        self.colors = ["green", "red", "yellow", "pink", "blue", "lightblue",
                       "orange", "purple", "black", "white"]
        self.fillcolors = ["green", "red", "yellow", "pink", "blue", "lightblue",
                       "orange", "purple", "black", "white"]
        self.shapes = ["turtle", "triangle", "circle", "square", "arrow", "classic"]
        self.settings = settings

        self.setup()

    def setup(self):
        self.t1.speed(0)
        self.t1.resizemode("auto")  # turtlesize increases with pensize
        self.t2.hideturtle()
        self.t3.hideturtle()
        self.t4.hideturtle()
        self.t5.hideturtle()
        self.t6.hideturtle()
        self.t7.hideturtle()
        self.t8.hideturtle()
        self.s.screensize(settings.get("screen_dims")[0],
                          settings.get("screen_dims")[1])  # space for turtle
        self.s.setup(settings.get("screen_dims")[0]*1.1,
                     settings.get("screen_dims")[1]*1.1)  # actual screen size
        self.s.cv._rootwindow.resizable(False, False)
        self.s.title(self.settings.get("title"))
        self.draw_color()
        self.v.draw_volume_bar()
        self.draw_toolbar()
        self.draw_shapes()
        self.refer_to_instructions()
        self.v.fill_volume_bar(self.t1.pensize()/self.settings.get("max_pensize"))
        self.set_pensize()
        self.register_callbacks()

    def register_callbacks(self):
        self.t1.onclick(self.t1.goto, 1)
        self.s.onkey(self.pen_change, "p")
        self.s.onkey(self.change_color, "space")
        self.s.onscreenclick(self.go_to, 1)
        self.t1.ondrag(self.go_to, 1)
        self.s.onkey(self.screen_exit_handler, "Escape")
        self.s.onkey(self.screen_save_handler, "s")
        self.s.onkeypress(self.undo_drawings, "u")
        self.s.onkey(self.clear_all, "c")
        self.s.onkey(self.change_shape, "t")
        self.s.onkeypress(self.move_down, "j")
        self.s.onkey(self.show_instrucions, "?")
        self.s.onkeypress(self.move_up, "k")
        self.s.onkeypress(self.turn_left, "h")
        self.s.onkeypress(self.turn_right, "l")
        self.s.onkey(self.t1.begin_fill, "b")
        self.s.onkey(self.t1.end_fill, "e")
        self.s.onkey(self.change_fillcolor, "f")
        self.s.listen()
     

    def screen_exit_handler(self):
        print("[debug] got ESC, quitting")
        exit(0)

    def screen_save_handler(self):
        print("[debug] trying to save canvas to a pdf file")
        name = self.s.textinput("Save a Screenshot to PDF",
                                "Please enter a filename (without .pdf): ")
        self.s.getcanvas().postscript(file="tmp.ps", colormode="color")
        if platform.system() == "Windows":
            cmd = r'c:\Program Files\Git\usr\bin\bash.exe'
            p = subprocess.Popen([cmd, "ps2pdf", "tmp.ps", "{}.pdf".format(name)],
                                shell=True)
        else:  # we're actually on a good OS here
            p = subprocess.Popen(["ps2pdf tmp.ps {}.pdf".format(name)],
                                shell=True)
        ret = p.wait()
        if ret == 0:
            os.remove("tmp.ps")
        self.s.listen()  # required to re-focus onto turtle

    def show_instrucions(self):
        win = Tk()

        row = 0
        column = 0
        for instruction in self.instructions:
            Label(win, text = instruction).grid(row = row, column = column, sticky = "W", ipadx = 10)
            column +=1
            Label(win, text = self.instructions.get(instruction)).grid(row = row, column = column, sticky = "W", ipadx = 10)
            row += 1
            column = 0

    def pen_change(self):
        self.toggler

        if self.t1.isdown():
            self.t1.penup()
            self.toggler.toggle()
        else:
            self.t1.pendown()
            self.toggler.toggle()

    def draw_selector(self, turtle, pensize):
        turtle.clear()
        turtle.pensize(pensize)
        for _ in range(4):
            turtle.fd(30)
            turtle.left(90)

    def draw_color(self):
        self.s.tracer(False)
        x = -410
        pos = (x, 310)
        self.t2.penup()
        self.t3.penup()
        self.t8.penup()
        self.t2.goto(pos)
        self.t3.goto(-50, 310)
        self.t8.goto(-35, 295)
        self.t2.right(90)
        self.t3.right(90)
        self.t2.pendown()
        self.t3.pendown()
        self.t8.pendown()
        self.t2.pensize(1)
        for color in self.colors:
            # determine colors
            if color == "white":
                self.t2.pencolor("black")
                self.t2.fillcolor("white")
            else:
                self.t2.color(color)

            # draw square
            self.t2.begin_fill()
            for _ in range(4):
                self.t2.fd(30)
                self.t2.left(90)

            # pen up, go to next square, pen down
            self.t2.end_fill()
            self.t2.penup()
            x += 40
            self.t2.goto(x, 310)
            self.t2.pendown()
        self.s.tracer(True)

    def change_color(self):
        if self.t3.pos()[0] >= -50:
            x = -410
        else:
            x = self.t3.pos()[0] + 40

        color = self.colors.pop(0)
        self.t1.pencolor(color)
        self.colors.append(color)
        self.s.tracer(False)

        if color == "black":
            self.t3.pencolor("dim gray")
        else:
            self.t3.pencolor("black")

        self.t3.penup()
        self.t3.goto(x, 310)
        self.t3.pendown()
        self.draw_selector(self.t3, 4)
        self.s.tracer(True)

    def change_fillcolor(self):
        self.s.tracer(False)
        if self.t8.pos()[0] >= -36:
            x = -395
        else:
            x = self.t8.pos()[0] + 40

        fillcolor = self.fillcolors.pop(0)
        self.t1.fillcolor(fillcolor)
        self.fillcolors.append(fillcolor)

        if fillcolor == "black":
            self.t8.pencolor("dim gray")
        else:
            self.t8.pencolor("black")

        self.t8.penup()
        self.t8.goto(x, 295)
        self.t8.pendown()
        self.t8.clear()
        self.t8.dot(10)
        self.s.tracer(True)


    def increase_pensize(self):
        pensize = self.t1.pensize() + self.settings.get("pensize_stepsize")
        if pensize <= self.settings.get("max_pensize"):
            self.t1.pensize(pensize)
            self.v.fill_volume_bar(
                self.t1.pensize()/self.settings.get("max_pensize"))

    def decrease_pensize(self):
        pensize = self.t1.pensize() - self.settings.get("pensize_stepsize")
        if pensize >= 1:
            self.t1.pensize(pensize)
            self.v.fill_volume_bar(
                self.t1.pensize()/self.settings.get("max_pensize"))

    def set_pensize(self):
        self.s.onkey(self.increase_pensize, "Up")
        self.s.onkey(self.decrease_pensize, "Down")

    def draw_toolbar(self):
        self.s.tracer(False)
        self.t4.penup()
        self.t4.goto(-420, 260)
        self.t4.pensize(3)
        self.t4.pendown()
        self.t4.fd(840)
        self.t4.penup()
        self.t4.goto(-420, -300)
        self.t4.pendown()
        self.t4.fd(840)
        self.s.tracer(True)

    def draw_shapes(self):
        self.s.tracer(False)
        self.t5.penup()
        self.t5.resizemode("user")
        self.t5.shapesize(0.9, 0.9)
        x = 200
        self.t5.fillcolor("white")
        
        for shape in self.shapes:
            self.t5.shape("turtle")
            self.t5.goto(x, 295)
            self.t5.shape(shape)
            self.t5.stamp()
            x += 40

        self.t6.penup()
        self.t6.goto(389, 280)

        self.s.tracer(True)

    def change_shape(self):
        self.s.tracer(False)
        shape = self.shapes.pop(0)
        self.t1.shape(shape)
        self.shapes.append(shape)

        if self.t6.pos()[0] >= 380:
            x = 189
        elif shape == "circle":
            x = self.t6.pos()[0] + 38
        elif shape == "arrow":
            x = self.t6.pos()[0] + 43
        elif shape == "classic":
            x = self.t6.pos()[0] + 32
        elif shape == "triangle":
            x = self.t6.pos()[0] + 39
        else:
            x = self.t6.pos()[0] + 40

        self.t6.penup()
        self.t6.goto(x, 280)
        self.t6.pendown()
        self.t6.pencolor("green")
        self.draw_selector(self.t6, 2)
        self.s.tracer(True)

    def refer_to_instructions(self):
        self.s.tracer(False)
        self.t7.penup()
        self.t7.goto(-410, -320)
        self.t7.pendown()
        self.t7.write("press '?' for instructions")
        self.s.tracer(True)


    def move_up(self):
        self.t1.fd(10)

    def move_down(self):
        self.t1.backward(10)

    def turn_left(self):
        heading = self.t1.heading()
        if heading == 355:
            self.t1.setheading(0)
        else:
            heading += 5
            self.t1.setheading(heading)

    def turn_right(self):
        heading = self.t1.heading()
        if heading == 0:
            self.t1.setheading(355)
        else:
            heading -= 5
            self.t1.setheading(heading)

    def go_to(self, x, y):
        if y < 258 and y > -300:
            self.t1.goto(x, y)

    def undo_drawings(self):
        self.t1.undo()

    def clear_all(self):
        self.t1.clear()
    
    def mainloop(self):
        mainloop()


if __name__ == "__main__":
    tpaint = TurtlePaint(settings)
    tpaint.mainloop()
