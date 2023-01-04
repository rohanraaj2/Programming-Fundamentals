n = int(input())
def int_to_string(n):
    if n >= 0:
        if n < 10:
            return (chr(n + 48))
        else:
            return (int_to_string(n // 10) + chr((n % 10) + 48))
    else:
        if n > -10:
            return (-chr(-n + 48))
        else:
            n = -n
            y = int_to_string(n)
            return ("-" + y)
import inspect
source = inspect.getsource(int_to_string)
if "for " in source or "while " in source:
  print("Try a recursive approach!")
else:
  result = int_to_string(n)
  if isinstance(result, str):
      print(result)
  else:
      print('Returned value is not a string.')
