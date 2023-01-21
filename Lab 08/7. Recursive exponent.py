a = int(input())
b = int(input())
def power(a, b):
 if b == 0:
 return 1
 elif b == 1 or a == 0:
 return a
 elif b > 0:
 return (a * power (a, b - 1))
 elif b < 0:
 return ((1 / a) * power (a, b + 1))
