import turtle
bob = turtle.Turtle()
bob.speed(6)
bob.shape("arrow")

#design 1: overlapping circles
for times in range(3):
     bob.circle(50)
     bob.forward(times * 5)
     bob.left(120)

bob.penup()
bob.goto(200,100)
bob.pendown()
bob.width(1)
     
#design 2: comet
for number in range(10):
  bob.width(number * 3)
  bob.forward(20)
  bob.left(6)

bob.penup()
bob.goto(-200,100)
bob.pendown()
bob.width(1)

#design 3: triangular spiral
for number in range(40):
  bob.forward(number * 4)
  bob.left(120)

bob.penup()
bob.goto(0,-200)
bob.pendown()
bob.width(1)

#design 4: square-like spiral
for number in range(40):
  bob.forward(number * 4)
  bob.left(91)
