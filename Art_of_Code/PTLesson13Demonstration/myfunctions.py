import turtle
bob = turtle.Turtle()

def polygon(sides,distance):
  angle = 360 / sides
  for times in range(sides):
    bob.forward(distance)
    bob.left(angle)
