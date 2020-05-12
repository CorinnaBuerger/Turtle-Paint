PAINT_TRTL = 0
STATUSBAR_TRTL = 1
COLOR_TRTL = 2
NUM_TRTLS = 3

def init_turtles:
    ts = []
    for _ in range(NUM_TRTLS):
        ts.append(Turtle())

    return ts

def get_turtle(self, selector):
    return self._turtles[selector]

tp = self.get_turtle(PAINT_TRTL)
tp.do_something()
tp.do_something_else()
tp.do_something_even_more()
