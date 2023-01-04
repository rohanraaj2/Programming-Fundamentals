d1, d2 = [eval(input()) for _ in range(2)]
def merge_key(d1,d2):
    l = []
    d = {}
    if len (d1) == len (d2):
        for i in range (1, len(d1) + 1):
            l = []
            x = d1.get(i)
            y = d2.get(i)
            l.append(x)
            l.append(y)
            d[i] = l
        return d
# Enter your code here.
print(sorted(merge_key(d1,d2).items()))
