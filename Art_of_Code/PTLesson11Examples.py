import turtle

bob = turtle.Turtle()
bob.speed(0)

#Example 1
for times in range(70):
     bob.circle(times * 5)
     bob.forward(times * 5)
     bob.left(120)
     
'''
#Example 2
for times in range(100):
     bob.circle(100)
     bob.forward(times * 5)
     bob.left(120)


#Example 3
for times in range(150):
     bob.circle(times*2)
     bob.forward(times*2)
     bob.left(91)


#Example 4
for times in range(500):
     bob.forward(15)
     bob.left(times * 7)

'''