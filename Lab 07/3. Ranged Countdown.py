def countdown2(a,b):
 if type (a) == float or type (b) == float:
 print ("Error: bad argument. countdown2 is defined for integers
only.")
 elif type (a) == int and type (b) == int:
 if b > a:
 for i in range (b, a, -1):
 print (i, end = ", ")
 print (a)

 elif a > b:
 for i in range (a, b, -1):
 print (i, end = ", ")
 print (b)
 elif a == b:
 print (a)
