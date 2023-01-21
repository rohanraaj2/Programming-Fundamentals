def fibonacci_sequence(a):
 if type (a) != int or a < 0:
 print ("Error: bad argument. fibonacci is defined for positive
integers only.")
 else:
 x = 0
 y = 1

 if a == 0:
 print (x)
 if a == 1:
 print (str(x) + ", " + str(y))
 if a > 1:
 print (str(x) + ", " + str(y), end = ", ")
 for i in range (a - 1):
 z = x + y
 x = y
 y = z
 if i == a - 2:
 print (y)
 else:
 print (y, end = ", ")
