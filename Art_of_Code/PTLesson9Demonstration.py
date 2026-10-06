import turtle

bob = turtle.Turtle()

bob.speed(10)
distance = 60

for times in range(4):
  bob.forward(distance)
  bob.left(90)
  bob.forward(distance)
  bob.right(90)
  bob.circle(30)
  bob.forward(distance)
  bob.left(90)
