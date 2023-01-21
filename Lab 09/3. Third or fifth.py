def third_or_fifth(s):
 result = ''
 index = 0
 while index < len(s):
 letter = s[index]
 if (index + 1) % 3 == 0 or (index + 1) % 5 == 0:
 result = result + letter
 index = index + 1
 return result
