d1, d2 = [eval(input()) for _ in range(2)]
def merge_value(d1,d2):
    d = {}
    l = []
    if len (d1) == len (d2):
        for i in range (len(d1) + 1):
            l = []
            if i in d1:
                x = d1.get(i)
                for k in d2:
                    if d2[k] == x:
                        l.append(i)
                        l.append(k)
                        d[x] = l
        return d
# Enter your code here.
print(sorted(merge_value(d1,d2).items()))
