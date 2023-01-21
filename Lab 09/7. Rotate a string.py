def rotate(s, n):
 while n > len (s):
 n = n - len (s)
 while n < - (len (s)):
 n = n + len(s)
 if n >= 0:
    x = s [n: len (s)]
 return (x + str(s[0:n]))
 elif n < 0:
 x = s [0 : n]
 return (str(s[len(s) + n] + x))
