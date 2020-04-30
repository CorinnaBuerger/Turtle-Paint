# Readme

TurtlePaint is a drawing program made with the Python Turtle. 
It allows you to draw nice pictures by clicking on the screen, moving the turtle around with <kbd>h</kbd>, <kbd>j</kbd>, <kbd>k</kbd>, <kbd>l</kbd> or by simply dragging it with your mouse. Choose between different pencolors, fillcolors, pensizes and turtle shapes to get a perfect result!
It is great for creating simple shapes, but also to free your creativity!

## Instructions

### Overview

Keys                  |                    Command
----------------------|---------------------------
<kbd>b</kbd>          |              begin filling
<kbd>c</kbd>          |                  clear all
<kbd>e</kbd>          |                end filling        
<kbd>f</kbd>          |           change fillcolor         
<kbd>h</kbd>          |                  turn left       
<kbd>j</kbd>          |              move backward        
<kbd>k</kbd>          |               move forward        
<kbd>l</kbd>          |                 turn right       
<kbd>p</kbd>          |          pen up / pen down       
<kbd>s</kbd>          |                       save         
<kbd>t</kbd>          |        change turtle shape       
<kbd>u</kbd>          |          undo last drawing       
<kbd>SPACE</kbd>      |            change pencolor         
<kbd>UP</kbd>         |           increase pensize       
<kbd>DOWN</kbd>       |           decrease pensize        
<kbd>?</kbd>          |          show instructions       

## Details
The following section gives detailed information on all key combinations and explains the program usage in greater detail:

### <kbd>b</kbd> 
Calls `turtle.begin_fill()`. Needs to be pressed **before** drawing the shape that needs filling. Otherwise the filling will be uncomplete. 

### <kbd>c</kbd>
Calls `turtle.clear()`. Erases everything that the turtle has drawn so far.

### <kbd>e</kbd>
Calls `turtle.end_fill()`. Needs to be pressed right after the shape is finished. You can still change the fillcolor right before --- even after you called `turtle.begin_fill()`.

### <kbd>f</kbd>
Calls `turtle.fillcolor()` with the next fillcolor in line. 

### <kbd>h</kbd>
With `turtle.setheading()` it sets the turtle's heading `5 px` to the left.

### <kbd>j</kbd>
Calls `turtle.backward(10)`. The turtle will go `10 px` backward.

### <kbd>k</kbd>
Calls `turle.forward(10)`. The turtle will go `10 px` forward.

### <kbd>l</kbd>
With `turtle.setheading()` it sets the turtle's heading `5 px` to the right.

### <kbd>p</kbd>
Toggles between `turtle.penup()` and `turtle.pendown()`. The turtle will only draw if the pen is down.

### <kbd>s</kbd>
Saves your picture as `.pdf` after you entered a name.

### <kbd>t</kbd>
Calls `turtle.shape()` with the next turtle shape in line.

### <kbd>u</kbd>
Calls `turtle.undo()` to erase the last thing the turtle has drawn.

### <kbd>SPACE</kbd>
Calls `turtle.pencolor()` with the next pencolor in line.

### <kbd>UP</kbd>
With `turtle.pensize()` it increases the pensize with `+2`.

### <kbd>DOWN</kbd>
With `turtle.pensize()` it decreases the pensize with `-2`.

### <kbd>?</kbd>
Shows all the instructions above in an additional window.

## License and Contribution
TODO