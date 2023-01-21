def countup_even(a,b):
 if type (a) == float or type (b) == float:
 print ("Error: bad argument. countup_even is defined for integers
only.")
 elif type (a) == int and type (b) == int:
 if b > a:
 if a % 2 == 1:
 a = a + 1
 if b % 2 == 1:
b = b - 1
        for i in range (a, b, 2):
 print (i, end = ", ")
 print (b)

 elif a > b:
 if b % 2 == 1:
 b = b + 1
 if a % 2 == 1:
 a = a - 1
 for i in range (b, a, 2):
 print (i, end = ", ")
 print (a)
 elif a == b:
 if a % 2 ==0:
 print (a)
