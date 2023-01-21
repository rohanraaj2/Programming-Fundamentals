a = int(input())
b = int(input())
def product(a, b):
 if b == 0:
 return 0
 elif (a < 0 and b < 0) or (a > 0 and b < 0):
 return (-a + int(product(a, b+1)))
 else:
 return (a + int(product(a, b-1)))
