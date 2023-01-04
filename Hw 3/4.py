def my_find(s, subs):
    x = 0
    l = len(subs)
    if l <= len(s):
        if subs in s:
            return(helper (s, subs, x))
        else:
            return -1
    
def helper (a, b, y):
    c = len(b)
    if a[0:c] == b:
        return y
    else:
        y += 1
        return(helper(a[1:],b,y))
import inspect, re
verboten_in_callable = ['[e]val', '[g]etattr', '[f]or.*:', '[w]hile.*:']
verboten_in_callable = [re.compile(pattern) for pattern in verboten_in_callable]
globals_copy = globals().copy()
if any(callable(value) and any(pattern.search(inspect.getsource(value))
                               for pattern in verboten_in_callable)
       for value in globals_copy.values()):
    print('Illegal statement found, please see the note in the description.')

s = input()
subs = input()
print(my_find(s, subs))
