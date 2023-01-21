def countdown (n):
 if type(n) == float or n < 0:
 print ("Error: bad argument. countdown is defined for positive
integers only.")
 else:
 for i in range (n, 0, -1):
 print (i, end = ", ")
 print (0)
