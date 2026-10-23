from myFunctions import *

#turtle.tracer(0) # draws with no animation
turtle.colormode(255)# sets color mode for (r,g,b)

bob.speed(0)
bob.width(1)

# pencolor and color apply to border only
#bob.pencolor("black")
bob.color("black")
'''
# ex1
for times in range( 256 ):
  c = ( times, 0, 0 )
  bob.fillcolor(c)
  bob.begin_fill()
  bob.circle( 50 )
  bob.end_fill() 

# ex2
for times in range( 256 ):
  c = ( times, 0, 0 )
  bob.fillcolor(c)
  bob.begin_fill()
  bob.circle( 30 )
  bob.end_fill()
  bob.forward(10)

# ex3
for times in range( 256 ):
  c = ( times, 0, 0 )
  polygon(3, 255 - times, c )

# ex4
for times in range( 256 ):
  c = ( times, 0, 255 - times )
  polygon(3, 100, c )
  bob.forward(10)


#==============================================
# gradient design 1 (black to green)
for times in range( 256 ):
  c = ( 0, times, 0 )
  polygon(4, 100, c )
  bob.left(3)
  bob.forward(5)



# gradient design 2 (red to black)
for times in range( 256 ):
  c = ( times, 0, 0 )
  polygon(3, 255 - times, c )
  bob.forward(10)
  bob.left(10)

'''
# gradient design 3
turtle.bgcolor("black")
for times in range( 256 ):
  c = ( times, 0, 255 - times )
  bob.color("yellow", c) # 1st border color, 2nd fill colors
  polygon(5, 40, c )
  bob.forward(times)
  bob.left(25)

