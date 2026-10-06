import turtle

bob = turtle.Turtle()

sides = 3
angle = 360 / sides
distance = 100

for times in range(sides):
    bob.forward(distance)
    bob.left(angle)
