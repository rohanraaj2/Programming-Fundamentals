def stretch(s):
 y = ""
 for i in range (0 , len(s)):
 x = s [i] * (i + 1)
 y = y + str(x)
 return y
