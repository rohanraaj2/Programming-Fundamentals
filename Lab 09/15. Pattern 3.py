n = int(input())
def pattern(n):
 l = 1
 i = 0
 while l <= n:
 i += 1
 if i < l * l:
 print (i, end = " ")

 else:
 l += 1
 print (i)
