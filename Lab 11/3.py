def remove_all(t, v):
    c = 0
    for i in t:
        if i == v:
            c += 1
    while v in t:
        t.remove(v)
    return c

if __name__ == '__main__':
    import inspect
    import re
    list_methods = ['__delitem', '__getitem__', '__setitem__']
    verboten_methods = ['\\.[ \\t]*' + method + '[ \\t]*\\('
                        for method in list_methods]
    verboten = ['eval', 'getattr', '\\[', '\\]']
    verboten.extend(verboten_methods)
    verboten = [re.compile(pattern) for pattern in verboten]
    globals_copy = globals().copy()
    if any(callable(value) and any(pattern.search(inspect.getsource(value))
                                   for pattern in verboten)
           for value in globals_copy.values()):
        print('eval function, getattr function, indexing, slicing, or internal list methods may not be used.')
    else:
        t = eval(input())
        v = eval(input())
        print(remove_all(t, v))
        print(t)
