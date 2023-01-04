def pick(k, t):
    if len(t) > 0:
        l = []
        for d in t:
            l.append(d[k])
        return l
k = eval(input().strip())
t = eval(input().strip())
print(pick(k, t))
