from myFunctions import *
# brings in everything ( * ) from the myFunctions file
# Note: do NOT put .py after filename above

bob.speed(0)

# draws one square with side length 100
square(100)

bob.penup()
bob.goto(250, 0)
bob.pendown()

# draws 20 squares and turns 92 degrees after each square
for times in range(20):
  square(100)
  bob.right(92) # turns after each square





