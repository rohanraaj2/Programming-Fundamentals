a = int(input())
b = int(input())
def modulus(a, b):
    if a > 0 and b > 0:
        c = a - b
        while c > b:
            c -= b
        if c < 0:
            return a
        else:
            return c
        

import inspect
source = inspect.getsource(modulus)
if "%" in source:
  print('Compute the modulus yourself!')
else:
  result = modulus(a, b)
  if isinstance(result, int):
    print(result)
  else:
    print('Bad return type.')
