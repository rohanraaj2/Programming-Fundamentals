n = int(input())
def pattern(n):
 r = "0"
 if n >= 1:
 for i in range (1 , n + 1):
 r = r + " " + str(i)
 if len(r) > 20:
 for j in range (len(r), 20, -3):
 print (r [0:j])
 for j in range (19, 2, -2):
 print (r [0:j])
 else:
 for j in range (len(r), 2, -2):
 print (r [0:j])
