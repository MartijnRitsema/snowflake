import turtle
import random

# set up the window with a background colour
wn = turtle.Screen()
wn.bgcolor("snow")

# assign a name to your turtle
martijn = turtle.Turtle()
martijn.speed(15)

# create a list of colours
sfcolor = ["green", "coral", "red", "grey", "blue"]

# create a function to create different size snowflakes
def snowflake(size):
    # move the pen into starting position
    martijn.penup()
    martijn.forward(10 * size)
    martijn.left(45)
    martijn.pendown()
    martijn.color(random.choice(sfcolor))
    # draw branch 8 times to make a snowflake
    for i in range(8):
        branch(size)
        martijn.left(45)


# create one branch of the snowflake
def branch(size):
    for i in range(3):
        for i in range(3):
            martijn.forward(10.0 * size / 3)
            martijn.backward(10.0 * size / 3)
            martijn.right(45)
        martijn.left(90)
        martijn.backward(10.0 * size / 3)
        martijn.left(45)
    martijn.right(90)
    martijn.forward(10.0 * size)

# loop to create 20 different sized snowflakes with different starting co-ordinates
for i in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    sf_size = random.randint(1, 4)
    martijn.penup()
    martijn.goto(x, y)
    martijn.pendown()
    snowflake(sf_size)

# leave the window open until you click to close
wn.exitonclick()