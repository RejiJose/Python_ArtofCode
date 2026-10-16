from myFunctions import *
bob.speed(10)

# draw one pentagon of side length 100
polygon(5, 100)

# draw 8 polygons with varying # of sides each of side length 50
for times in range(8):
  polygon(times + 3, 50)

