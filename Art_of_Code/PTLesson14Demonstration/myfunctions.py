import turtle
bob = turtle.Turtle()

def comet(distance, angle):
  for times in range(10):
    bob.width(times)
    bob.forward(distance)
    bob.left(angle)

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()

