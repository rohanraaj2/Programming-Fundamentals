def last_name_first(t):
    for j in range(len(t)):
        t[j] = (t[j][-1],) + (t[j][:-1])


t = eval(input())
last_name_first(t)
print(t)
