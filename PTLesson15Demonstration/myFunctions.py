import turtle
bob = turtle.Turtle()

def polygon(sides, dist, color):
  angle = 360/sides
  bob.fillcolor(color) # fills in a color
  bob.begin_fill()
  for times in range(sides):        
    bob.forward(dist)
    bob.left(angle)
  bob.end_fill()

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()