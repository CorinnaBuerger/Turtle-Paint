from sys import exit
from turtle import Screen, Turtle, mainloop

from libturtle import StringToggler, VolumeBar

settings = {
    "start_volume_bar": (80, 280),
    "start_penup": (0, 300),
    "start_pendown": (0, 280),
    "max_pensize": 21,
    "pensize_stepsize": 2,
    "title": "Turtle Paint v0.0.2"
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
        self.t3.hideturtle()
        self.s.screensize(600, 600)
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

    def screen_exit_handler(self):
        print("[debug] got ESC, quitting")
        exit(0)

    def pen_change(self, xdummy, ydummy):
        self.toggler

        if self.t1.isdown():
            self.t1.penup()
            self.toggler.toggle()
        else:
            self.t1.pendown()
            self.toggler.toggle()

    def draw_selector(self):
        self.t3.clear()
        self.t3.pensize(4)
        for _ in range(4):
            self.t3.fd(30)
            self.t3.left(90)

    def draw_color(self):
        self.s.tracer(False)
        x = -370
        pos = (x, 310)
        self.t2.penup()
        self.t3.penup()
        self.t2.goto(pos)
        self.t3.goto(-50, 310)
        self.t2.right(90)
        self.t3.right(90)
        self.t2.pendown()
        self.t3.pendown()
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

    def return_pos_click(self):
        self.s.onscreenclick(self.t2.goto)
        return self.t2.pos()

    def change_color(self):
        if self.t3.pos()[0] >= -50:
            x = -370
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
        self.draw_selector()
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
