s1 = input()
s2 = input()
def common (s1, s2):
 b = 0
 x = ""
 for i in range(len(s1)):
 for j in range (len(s2)):
 if s1[i] == s2[j]:
 a = s1[i]
 b = 0
  for k in range (len(x)):
 if a == x[k]:
 b = 1
 if b == 0:
 x = x + str(a)
 return x
