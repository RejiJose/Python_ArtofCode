# This myFunctions.py file defines all the functions
# it has the 'import turtle' and creates a bob turtle object

import turtle
bob = turtle.Turtle()

# we define a function using the keyword "def"
# def is followed by the function name
# all function names are followed by () parentheses
def square(dist):
  for times in range(4):
    bob.forward(100)
    bob.left(90)