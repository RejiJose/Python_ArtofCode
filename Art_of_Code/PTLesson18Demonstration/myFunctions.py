import turtle
bob = turtle.Turtle()

# Tree type 1  
def tree1(x,y):
  jump(x,y)
  bob.pensize(5)
  bob.color("brown")
  polygon(4, 50)#square(trunk of tree)
  jump(-25 + x , 50 + y)
  bob.color("green")
  polygon(3, 100)#1st triangle(tree top)
  jump(-25 + x, 75 + y)
  polygon(3, 100)#2nd triangle(tree top)

# Tree type 2
def tree2(x,y):
  jump(x,y)
  bob.pensize(5)
  bob.color("brown")
  polygon(4, 50)
  bob.color("green")
  
  jump(-10 + x, 50 + y)
  bob.begin_fill()
  bob.circle(40)
  bob.end_fill()
  
  jump(60 + x, 50 + y)
  bob.begin_fill()
  bob.circle(40)
  bob.end_fill()
  
  jump(25 + x, 75 + y)
  bob.begin_fill()
  bob.circle(40)
  bob.end_fill()
  
  jump(25 + x, 25 + y)
  bob.begin_fill()
  bob.circle(40)
  bob.end_fill()

# Sun design
def sun(x,y):
  jump(x,y)
  bob.pensize(10)
  bob.color("yellow")
  for times in range(10):
    polygon(3,20)
    bob.forward(30)
    bob.right(36)
  jump(16 + x,-75 + y)
  bob.pensize(20)
  bob.circle(30)

def polygon(sides, dist):
  angle = 360/sides
  bob.begin_fill()
  for times in range(sides):        
    bob.forward(dist)
    bob.left(angle)
  bob.end_fill()

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()
  
def comet(c, distance, angle):
  bob.color(c)
  for times in range(10):
    bob.pensize(times)
    bob.forward(distance)
    bob.left(angle)

def rainbow(x,y):
  jump(x,y)
  bob.width(20)
  bob.color("red")
  bob.left(90)
  bob.circle(-60, 180)
  # circle with neg radius = clockwise
  # circle with 2nd value = arc (180 is semi-circle)
  
  jump(x,y)
  bob.setheading(0) # sets turtle direction
  bob.penup()  
  bob.forward(10)
  bob.pendown()
  bob.left(90)
  bob.color("orange")  
  bob.circle(-50, 180)
  
  jump(x,y)
  bob.setheading(0)
  bob.penup()
  bob.forward(20)
  bob.pendown()
  bob.left(90)
  bob.color("yellow")
  bob.circle(-40, 180)
  
  jump(x,y)
  bob.setheading(0)
  bob.penup()
  bob.forward(30)
  bob.pendown()
  bob.left(90)
  bob.color("green")
  bob.circle(-30, 180)
  
  jump(x,y)
  bob.setheading(0)
  bob.penup()
  bob.forward(40)
  bob.pendown()
  bob.left(90)
  bob.color("blue")
  bob.circle(-20, 180)
  
  jump(x,y)
  bob.setheading(0)
  bob.penup()
  bob.forward(50)
  bob.pendown()
  bob.left(90)
  bob.color("purple")
  bob.circle(-10, 180)


def goto_home():
  bob.penup()
  bob.home()  
  bob.pendown()
  
def plus(c,distance):
  bob.color(c)
  for times in range(4):
    bob.forward(distance)
    bob.left(90)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(90)
    
    