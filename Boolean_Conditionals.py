from learntools.core import binder; binder.bind(globals())
from learntools.python.ex3 import *

# 1 

# Your code goes here. Define a function called 'sign'

def sign(n):
    
    if n == 0:
        return 0
    elif n < 0:
        return - 1
    else:
        return 1
    

# Check your answer

q1.check()

# 2

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    
    if total_candies > 1:
        print("Splitting", total_candies, "candies")
        return total_candies % 3
    else:
        print("There's only one candy")

to_smash(91)
to_smash(1)

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False 
rain_level = 0.0
have_hood = False
is_workday = False 

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

# Check your answer
q3.check()

# 4

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return True and number < 0 # Your code goes here (try to keep it to one line!)


# Check your answer
q4.check()