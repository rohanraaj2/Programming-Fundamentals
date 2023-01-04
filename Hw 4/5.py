def transmogrify():
    n = int(input())
    y = ""
    d ={}
    if n >= 0:
        for i in range(n):
            x = input()
            d[x[0]] = x[2]
        x = input()
        for j in x:
            y += d[j]
    return y

print(transmogrify())
