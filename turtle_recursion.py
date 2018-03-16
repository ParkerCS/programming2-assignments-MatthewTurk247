import turtle
import math

'''
Turtle Recursion (33pts)

1)  Using the turtle library, create the H fractal pattern according to the file shown in the data folder. (15pts)
'''
# assign a color for each depth
pen = turtle.Turtle()
pen.speed(0)
pen.shape('turtle')
pen.showturtle()
# pen.hideturtle()
my_screen = turtle.Screen()
my_screen.bgcolor('white')
pen.fillcolor('black')
pen.color('black')
pen.width(2)

pen.begin_fill() # starting a new object that we will fill in
# The size of the screen is 215 in each direction

pen.up()
pen.goto(0, 0)
pen.down()

def recursive_h(turtle, depth, center, length):

    if depth < 0:
        return

    if center is not None:
        turtle.up()
        turtle.goto(center)
        turtle.down()

    turtle.forward(length / 2)
    turtle.right(90)
    turtle.forward(length / 2)
    turtle.left(90)

    recursive_h(turtle, depth - 1, None, length / 2)

    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)

    recursive_h(turtle, depth - 1, None, length / 2)

    turtle.right(90)
    turtle.forward(length / 2)
    turtle.right(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length / 2)
    turtle.right(90)

    recursive_h(turtle, depth - 1, None, length / 2)

    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)

    recursive_h(turtle, depth - 1, None, length / 2)

    turtle.right(90)
    turtle.forward(length / 2)
    turtle.left(90)
    turtle.forward(length / 2)  # always leave the turtle where you found it!

recursive_h(pen, 3, (0, 0), 400)
my_screen.clear()

'''
2)  Using the turtle library, create any of the other recursive patterns in the data folder. 
Challenge yourself to match your pattern as closely as you can to the image.  (15pts)
Note:  The Koch snowflake shows step by step building of the fractal.  
       The rectangle fractal example shows 4 possible drawings of the same fractal (choose any one)
'''

'''
The relationship between the two triangles is that if you shade in all the odd numbers in Pascal's Triangle in one
color and leave the even numbers in another color, it makes Sierpinski's Triangle. No wonder I got them mixed up!
—Matthew
'''

def draw_sierpinski(length, depth):
    if depth > 0:
        draw_sierpinski(length/2, depth - 1)
        pen.forward(length/2)
        draw_sierpinski(length/2, depth - 1)
        pen.left(120)
        pen.forward(length/2)
        pen.right(120)
        draw_sierpinski(length / 2, depth - 1)
        pen.right(120)
        pen.forward(length/2)
        pen.left(120)
    else:
        pen.forward(length)
        pen.left(120)
        pen.forward(length)
        pen.left(120)
        pen.forward(length)
        pen.left(120)
    # call itself 3 times
    # draw big triangle
    # go to each midpoint and do the triangle and pass in the midpts

pen.up()
pen.goto(-250, -250)
pen.down()
draw_sierpinski(500, 5)
my_screen.clear()

'''
3)  Create your own work of art with a repeating pattern of your making.  
It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  
Take this one as seriously as the points indicate.  Play around.  (3pt) 

Give all your fractals a depth of at least 4.  Ensure the recursive drawing is contained on the screen (at whatever size you set it).
All three recursive drawings can be on the same program.  Just use screen.clear() between problems.
 Have fun!
 
 Resource to help you out >>> https://docs.python.org/3.3/library/turtle
'''

pen.goto(0, 0)
pen.showturtle()
pen.fillcolor('black')
pen.color('black')
pen.width(2)
pen.begin_fill()
def custom_fractal(length, depth):
    if depth > 0:
        for i in range(6):
            pen.forward(length)
            custom_fractal(length // 3, depth - 1)
            pen.backward(length)
            pen.left(60)

custom_fractal(200, 4)

my_screen.exitonclick()