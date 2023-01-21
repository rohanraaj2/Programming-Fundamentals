def slow_conceal(s):
 a = len(s)
 print (s[0: a])
 a -= 1
 if a > 0:
 slow_conceal(s[0 : a])
s = input().strip()
slow_conceal(s)
