[a,b,c] = [int(x) for x in input().strip().split()]
import math
def quadratic_roots (a, b, c):
 d = b*b - 4*a*c
 smaller = (- b - math.sqrt(d)) / (2*a)
 bigger = (- b + math.sqrt(d)) / (2*a)
 print("Equation:" + str(a)+ "x^2 +", str(b) + "x +", str(c), "= 0",
"\nRoots:", smaller, ",", bigger)
quadratic_roots (a, b, c)
