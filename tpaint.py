import os
import subprocess
from sys import exit
from turtle import Screen, Turtle, mainloop

from libturtle import StringToggler, VolumeBar

settings = {
    "start_volume_bar": (-370, 250),
    "start_penup": (0, 300),
    "start_pendown": (0, 280),
    "max_pensize": 21,
    "pensize_stepsize": 2,
    "title": "Turtle Paint v0.0.2",
    "screen_dims": (800, 600),
}


class TurtlePaint():
    def __init__(self, settings):
        self.t1 = Turtle()  # main turtle
        self.t2 = Turtle()  # draws color bar
        self.t3 = Turtle()  # selects a color from the color bar
        self.s = Screen()
        self.v = VolumeBar(settings.get("start_volume_bar"),
                           settings.get("max_pensize"), self.s)
        self.toggler = StringToggler(settings.get("start_penup"),
                                     settings.get("start_pendown"),
                                     "pen down", "pen up", self.s)
        self.colors = ["green", "yellow", "pink", "blue", "lightblue",
                       "orange", "purple", "black", "white"]
        self.settings = settings

        self.setup()

    def setup(self):
        self.t1.shape("turtle")
        self.t1.resizemode("auto")  # turtlesize increases with pensize
        self.t2.hideturtle()
        self.s.screensize(settings.get("screen_dims")[0],
                          settings.get("screen_dims")[1])  # space for turtle
        self.s.setup(settings.get("screen_dims")[0]*1.1,
                     settings.get("screen_dims")[1]*1.1)  # actual screen size
        self.s.title(self.settings.get("title"))
        self.draw_color()
        self.v.draw_volume_bar()
        self.v.fill_volume_bar(
            self.t1.pensize()/self.settings.get("max_pensize"))
        self.return_pos_click()
        self.set_color()
        self.set_pensize()
        self.register_callbacks()

    def register_callbacks(self):
        self.t1.onclick(self.t1.goto, 1)
        self.t1.onclick(self.pen_change, 3)
        self.s.onscreenclick(self.t1.goto, 1)
        self.s.onkey(self.screen_exit_handler, "Escape")
        self.s.onkey(self.screen_save_handler, "s")

    def screen_exit_handler(self):
        print("[debug] got ESC, quitting")
        exit(0)

    def screen_save_handler(self):
        print("[debug] trying to save canvas to a pdf file")
        name = self.s.textinput("Save a Screenshot to PDF",
                                "Please enter a filename (without .pdf): ")
        self.s.getcanvas().postscript(file="tmp.ps", colormode="color")
        p = subprocess.Popen(["ps2pdf tmp.ps {}.pdf".format(name)],
                             shell=True)
        p.wait()
        os.remove("tmp.ps")
        self.s.listen()

    def pen_change(self, xdummy, ydummy):
        self.toggler

        if self.t1.isdown():
            self.t1.penup()
            self.toggler.toggle()
        else:
            self.t1.pendown()
            self.toggler.toggle()

    def draw_color(self):
        self.s.tracer(False)
        x = -370
        pos = (x, 310)
        self.t2.penup()
        self.t3.penup()
        self.t2.goto(pos)
        self.t3.goto(pos)
        self.t2.right(90)
        self.t3.right(90)
        self.t2.pendown()
        self.t3.pendown()
        self.t2.pensize(1)
        self.t3.pensize(5)
        for _ in range(4):
            self.t3.fd(30)
            self.t3.left(90)
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

    def return_pos_click(self):
        self.s.onscreenclick(self.t2.goto)
        return self.t2.pos()

    def change_color(self):
        color = self.colors.pop(0)
        self.t1.pencolor(color)
        self.colors.append(color)
        self.t3.pensize(3)
        self.s.tracer(False)
        if color == "black":
            self.t3.pencolor("dim gray")
        else:
            self.t3.pencolor("black")
        self.t3.penup()
        self.t3.goto

        self.s.tracer(True)

    def set_color(self):
        self.s.onkey(self.change_color, "space")
        self.s.listen()

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

    def mainloop(self):
        mainloop()


if __name__ == "__main__":
    tpaint = TurtlePaint(settings)
    tpaint.mainloop()
