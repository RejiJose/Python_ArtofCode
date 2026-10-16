import turtle
bob = turtle.Turtle()

# comet fn to draw a comet shape
# pensize/width increases
def comet(distance, angle):
  for times in range(10):
    bob.width(times)
    bob.forward(distance)
    bob.left(angle)

# jump fn to relocate turtle to any (x,y) coordinate
def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()

