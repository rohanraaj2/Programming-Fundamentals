n = int(input())
def countdown (n):
 if n == 1:
 print (n)
 else:
 print (n, end = ", ")
 countdown (n - 1)
# Enter your code here.
import inspect
source = inspect.getsource(countdown)
if 'for' in source or 'while' in source:
 print('Try to solve the problem recursively!')
else:
 countdown(n)
