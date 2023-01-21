a = int(input())
b = int(input())
def countup (a,b):
 if b > a:
 print (a, end = ", ")
 countup (a + 1, b)
 if b == a:
 print (a)
