def lucas_term(n):
 if type (n) != int or n < 0:
 print ("Error: bad argument. lucas_term is defined for positive
integers only.")
 else:
        a = 2
 b = 1
 if n == 0:
 return a
 elif n == 1:
 return b
 else:
 for i in range (n - 1):
 if n > 1:
 c = a + b
 a = b
 b = c
 return (c)
