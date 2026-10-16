import turtle
bob = turtle.Turtle()

# general function for any shape
# polygon is the fn name
# sides and distance are the fn parameters
# angle is a fn variable

def polygon(sides,distance):
  angle = 360 / sides
  for times in range(sides):
    bob.forward(distance)
    bob.left(angle)
