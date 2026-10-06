import turtle

bob = turtle.Turtle()
bob.speed(10)

for number in range(10):
  bob.width(number * 3)
  bob.forward(20)
  bob.left(6)

bob.penup()
bob.goto(-200,100)
bob.pendown()
bob.width(1)

for number in range(80):
  bob.forward(number * 4)
  bob.left(120)

bob.penup()
bob.goto(0,-200)
bob.pendown()
bob.width(1)

for number in range(80):
  bob.forward(number * 4)
  bob.left(91)
