import random
from turtle import *

# making our turtle object called rishi
rishi = Turtle()

# making our screen object called my_screen
my_screen = Screen()

# listen function is added
my_screen.listen()

# adding colormode to screen
my_screen.colormode(255)


# function used to move right
def right():
    rishi.forward(10)


# funtion used to move left
def left():
    rishi.backward(10)


# function used to rotate anticlockwise
def up():
    rishi.left(5)


# function used to rotate clockwise
def down():
    rishi.right(5)


# function which add random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)
    return my_color

def ran_color():
    rishi.color(random_color())


# funtion used to pen up the turtle
def pen_up():
    rishi.penup()


# function used to pen down the turtle
def pen_down():
    rishi.pendown()


# function used to clear the screen
def clear_screen():
    rishi.clear()
    rishi.penup()
    rishi.home()
    rishi.pendown()

# function used to change the shape of the turtle
shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
def shape_change():
    random_shape = random.choice(shapes)
    rishi.shape(random_shape)


# press "d" to move forward
my_screen.onkey(right, "d")

# press "a" to turn backward
my_screen.onkey(left, "a")

# press "w" to turn up
my_screen.onkey(up, "w")

# press "s" to turn down
my_screen.onkey(down, "s")

# press "space" to pen up
my_screen.onkey(pen_up, "space")

# press "b" to pen down
my_screen.onkey(pen_down, "b")

# press "c" to change color
my_screen.onkey(ran_color,"c")

# press "x" to clear the screen and get back the turtle to the home
my_screen.onkey(clear_screen,"x")

# press "r" to change the shape of the turtle
my_screen.onkey(shape_change,"r")

my_screen.exitonclick()
