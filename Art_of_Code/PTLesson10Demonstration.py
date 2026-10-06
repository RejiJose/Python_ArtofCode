import turtle

bob = turtle.Turtle()

for number in range(10):
  print(number, number * 5, number * 5 + 5)
  bob.circle(number * 5 + 5)
