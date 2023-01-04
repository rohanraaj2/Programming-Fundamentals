#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'leap_years' function below.
#
# The function accepts following parameters:
#  1. INTEGER starting_year
#  2. INTEGER number_of_years
#
def leap_years(starting_year, number_of_years):
    print("Year Leap")
    print("---- ----")
    for i in range (starting_year, starting_year + number_of_years):
        if (i % 4 == 0 and i % 100 != 0) or (i % 100 == 0 and i % 400 == 0):
            print (i, "Yes")
        else:
            print (i, "No")

if __name__ == '__main__':
    starting_year = int(input().strip())

    number_of_years = int(input().strip())

    leap_years(starting_year, number_of_years)
