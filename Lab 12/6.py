# Enter your code here.
def count_words(s):
    n = []
    d = {}
    l = s.split()
    for i in l:
        p = ""
        if type (i) == str:
            i = i.lower()
        for k in i:
            if ord (k) > 96 and ord (k) < 123 or (ord (k) > 47 and ord (k) < 58):
                p += k
        if p != "":
            n.append(p)
        n.sort()
    for m in n:
        if m not in d:
            d[m] = 1
        else:
            d[m] += 1
    for o in d:
        print (o, "=", d[o])
    
count_words(input())
