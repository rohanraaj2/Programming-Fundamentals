def is_right_triangle(x, y, z):
 if x ** 2 == (y ** 2) + (z ** 2) or y ** 2 == x ** 2 + (z ** 2) or z ** 2
== x ** 2 + (y ** 2):
 return "True"
 else:
 return "False"
