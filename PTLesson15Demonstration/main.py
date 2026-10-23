from myFunctions import *

turtle.tracer(0) # draws with no animation
turtle.colormode(255) # sets color mode for (r,g,b)

bob.speed(0)
bob.width(1)

# pencolor and color apply to border only
#bob.pencolor("black")
bob.color("black")

# draw and fill in a single polygon
#polygon(6, 100, "yellow")


# draw and fill in many polygons
polygon(3, 50, "yellow")
jump(100, 0)

polygon(4, 50, "blue")
jump(200, 0)

polygon(5, 50, "cyan")
jump(100, 100)

polygon(6, 40, "green")
jump(-100, 0)

polygon(7, 40, "purple")
jump(-200, 0)

polygon(8, 40, "red")
jump(-200, -150)

# use loop to draw polygons
jump(-100, 250)
for times in range(8):
  c = (times *50, 0, 0)
  polygon(times+3, 30, c)
  bob.penup()
  bob.forward(50)
  bob.pendown()
