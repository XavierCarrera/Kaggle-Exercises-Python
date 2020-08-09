from learntools.core import binder; binder.bind(globals())
from learntools.python.ex5 import *

## 1

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    
    for num in nums:
        if num % 7 == 0:
            return True
        
    return False

# Check your answer
q1.check()

## 2

