from myFunctions import *
bob.speed(10)

# draw multiple comet shapes all starting from the origin
for times in range(11):
  jump(0,0)
  comet(5,10)
  bob.left(30)

