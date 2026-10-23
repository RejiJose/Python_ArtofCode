import turtle
bob = turtle.Turtle()

def circle(radius, border_color, fill_color):
  bob.pencolor(border_color)
  bob.fillcolor(fill_color)
  bob.begin_fill()
  bob.circle(radius)
  bob.end_fill()
  
def polygon(sides, dist, color):
  angle = 360/sides
  bob.fillcolor(color)
  bob.begin_fill()
  for times in range(sides):        
    bob.forward(dist)
    bob.left(angle)
  bob.end_fill()

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()
  
