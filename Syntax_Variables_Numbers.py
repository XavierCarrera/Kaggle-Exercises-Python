from learntools.core import binder; binder.bind(globals())
from learntools.python.ex1 import *

pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
____

# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
____

radius = diameter / 2

area = pi * (radius **2)

# Check your answer
q1.check()

########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about 
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]
q2.store_original_ids()
######################################################################

# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.

c = a
d = b
a = d
b = c

######################################################################

# Check your answer
q2.check()