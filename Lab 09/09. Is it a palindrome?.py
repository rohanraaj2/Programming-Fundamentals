def is_palindrome(s):
 a= ""
 l = len (s)
 for i in range (1, l):
 a = a + str(s[-i])
 a = a + str(s[0])
 if a == s:
 return True
 else:
 return False
