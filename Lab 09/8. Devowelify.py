def devowelify(s):
 x = ""
 for i in range (0 , len (s)):
 if s[i] != "a" and s[i] != "e" and s[i] != "i" and s[i] != "o" and
s[i] != "u" and s[i] != "A" and s[i] != "E" and s[i] != "I" and s[i] != "O"
and s[i] != "U":
 x = x + str(s[i])
 return x
