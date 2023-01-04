def pick(t, col):
    x = []
    for i in t:
        x.append(i[col])
    return x

t = eval(input())
col = int(input())
print(pick(t, col))
print(t)
