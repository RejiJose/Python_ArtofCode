from myFunctions import *
turtle.bgcolor("lightblue")
bob.speed(10)

tree1(-100,0)

tree2(20,50)

# forest of trees(both types) 
for times in range(3):
  tree1(-400 + times * 300, -100)
  tree2(-250 + times * 300, -100)


sun(350,300)

rainbow(-300, 150)

