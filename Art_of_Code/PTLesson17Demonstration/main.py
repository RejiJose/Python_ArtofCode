from myFunctions import *

# from random import *
# OR: from random import randint
# OR: import random [ if so, Must use random.randint() to generate numbers ]

turtle.colormode(255)
# turtle.tracer(0)
bob.speed(0)
bob.width(2)


# circles design 1  ===========  random # of circles
turtle.bgcolor("cyan")
num = randint(2, 8)
border = "red"
fill = (255, 255, 0)

for times in range( num ):
  circle(20, border, fill )
  bob.forward(50)
  bob.right(15)


# circles design 2  ============ random fill colors
turtle.bgcolor("black")
num = randint(10, 20)
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)
border = "yellow"
fill = (r,g,b)

for times in range( num ):
  circle(20, border, fill )
  bob.forward(50)
  bob.right(20)


# circles design 3  ============
# random # of circles at random locations with random sizes & random fill colors
turtle.bgcolor("black")
num = randint(100, 200)

for times in range( num ):
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  border = "cyan"
  fill = (r,g,b)
  x = randint(-300, 300)
  y = randint(-300, 300)
  radius = randint(5, 30)
  circle(radius, border, fill )
  jump(x,y)
