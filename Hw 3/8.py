#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'arrangement' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING letters as parameter.
#

def arrangement(letters):
    n = ""
    s = ""
    for x in letters:
        if x.upper() not in n.upper():
            n += x
    n = n.upper()
    if len(n) > 3:
        for i in n:
            for j in n:
                if j != i:
                    for k in n:
                        if k != i and k != j:
                            for l in n:
                                if l != i and l != j and l != k:
                                    c = i+j+k+l
                                    if c not in s:
                                        s += (c + ",")
        return s
    else:
        return ""
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    letters = input()

    res = arrangement(letters)
    resLst = res.split(",")
    cleanLst = list(filter(None, resLst))
    joinStr = "\n".join(sorted(cleanLst))

    fptr.write(joinStr + '\n')

    fptr.close()
