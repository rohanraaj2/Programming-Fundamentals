#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pattern' function below.
#.
#

def pattern(n):
    c = 1
    if n > 100000:
        print ("Program can't handle this input")
        return
    if type (n) != int or n < 0:
        print ("Invalid input")
    else:
        helper (n, c)
        
        
def helper (x, c):
    if x > 0:
        print ((" " * ((x - 1) * 2)) + ("* " * c))
        helper (x - 1, c +1)
import inspect
if __name__ == '__main__':
    n = int(input().strip())
    source = inspect.getsource(pattern)
    if "for " in source or "while " in source:
      print("Try a recursive approach!")
    else:
      pattern(n)
