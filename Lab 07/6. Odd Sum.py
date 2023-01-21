def sum_odd(a,b):
 k = 0
 if type (a) == float or type (b) == float:
 print ("Error: bad argument. sum_odd is defined for integers only.")
 elif type (a) == int and type (b) == int:
 if b > a:
 if a % 2 == 0:
 a = a + 1
 if b % 2 == 0:
 b = b - 1
 for i in range (a, b, 2):
 k = k + i
 return (k + b)

 elif a > b:
 if b % 2 == 0:
 b = b + 1
 if a % 2 == 0:
 a = a - 1
 for i in range (b, a, 2):
 k = k + i
 return (k + a)
 elif a == b:
 if a % 2 == 1:
 return (a)
 elif a % 2 == 0 and b % 2 == 0:
 return (0)
