a = int(input())
b = int(input())
def sum_odd(a,b):
 if a != b:
 if a % 2 == 0:
 a = a + 1
 if b % 2 == 0:
 b = b - 1
 if b > a:
 return ((int(a)) + int(sum_odd (a + 2, b)))
 elif a == b:
 if a % 2 == 0:
 return 0
 else:
 return (a)
