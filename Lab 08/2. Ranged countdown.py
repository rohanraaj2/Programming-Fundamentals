a = int(input())
b = int(input())
def countdown2(a, b):
 if b > a:
 print (b, end = ", ")
 countdown2 (a, b - 1)
 if b == a:
 print (b)
