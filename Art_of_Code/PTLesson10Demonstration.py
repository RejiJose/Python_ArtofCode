import turtle
bob = turtle.Turtle()
#1
for number in range(10):
  print(number)
#2
for number in range(10):
  print(number * 5)
#3
for number in range(10):
  print(number * 5 + 5)
#4
for number in range(10):
  print(number, number * 5, number * 5 + 10)
  bob.circle(number * 5 + 10)
