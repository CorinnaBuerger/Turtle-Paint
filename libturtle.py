from turtle import Screen, Turtle


class VolumeBar():
    def __init__(self, pos, maximum, screen):
        self.bar = Turtle()
        self.fill = Turtle()
        self.bar_hypo = 100
        self.pencolor = "black"
        self.pensize = 1
        self.pos = pos
        self.maximum = maximum
        self.s = screen

    def draw_volume_bar(self):
        self.bar.hideturtle()
        self.s.tracer(False)
        self.bar.pencolor(self.pencolor)
        self.bar.pensize(self.pensize)
        self.bar.penup()
        self.bar.goto(self.pos)
        self.bar.pendown()
        self.bar.left(10)
        self.bar.fd(self.bar_hypo)
        self.bar.right(100)
        self.bar.fd(self.maximum)
        self.bar.right(90)
        self.bar.goto(self.pos)
        self.s.tracer(True)

    def fill_volume_bar(self, percent=None):
        self.fill.hideturtle()
        self.fill.clear()
        self.s.tracer(False)
        forward = self.bar_hypo * percent
        down = self.maximum * percent
        self.fill.pencolor(self.pencolor)
        self.fill.fillcolor(self.pencolor)
        self.fill.penup()
        self.fill.goto(self.pos)
        self.fill.pendown()
        self.fill.begin_fill()
        self.fill.left(10)
        self.fill.fd(forward)
        self.fill.right(100)
        self.fill.fd(down)
        self.fill.right(90)
        self.fill.goto(self.pos)
        self.fill.right(180)
        self.fill.end_fill()
        self.s.tracer(True)


class StringToggler():
    def __init__(self, pos_first, pos_second, str_1, str_2, screen):
        self.write_turtle = Turtle()
        self.non_active_color = "light gray"
        self.active_color = "black"
        self.active_str = (str_1, pos_first)
        self.passive_str = (str_2, pos_second)
        self.font = 'Courier', 10, 'italic'
        self.write_turtle.hideturtle()
        self.s = screen
        self.write()

    def write(self):
        # write strings
        self.s.tracer(False)
        self.write_turtle.clear()
        self.write_turtle.penup()
        self.write_turtle.goto(self.active_str[1])
        self.write_turtle.pendown()
        self.write_turtle.color(self.active_color)
        self.write_turtle.write(self.active_str[0], font=self.font)
        self.write_turtle.penup()
        self.write_turtle.goto(self.passive_str[1])
        self.write_turtle.pendown()
        self.write_turtle.color(self.non_active_color)
        self.write_turtle.write(self.passive_str[0], font=self.font)
        self.s.tracer(True)

    def toggle(self):
        # toggle strings
        self.active_str, self.passive_str = self.passive_str, self.active_str
        self.write()
