import ast
st = input()
st = ast.literal_eval(st)

def count_char(s):
    if type(s) != str:
        return ("Error: bad argument. Function 'count_char' only accepts strings.")
    else:
        a = s.lower()
        y = []
        z = []
        h = ""
        for i in a:
            y = []
            x = 0
            if i not in h:
                for j in range (len(s)):
                    if i in a[j]:
                        x += 1
                h += i
                y.append(i)
                y.append(x)
                z.append(y)
    return z        
# Enter your code here.

print(count_char(st))
