# Enter your code here.
def count_words(s):
    n = []
    d = {}
    l = s.split()
    t = 1
    for i in l:
        p = ""
        if type (i) == str:
            i = i.lower()
        for k in i:
            if ord (k) > 96 and ord (k) < 123 or (ord (k) > 47 and ord (k) < 58):
                p += k
        if p not in n and p != "":
            n.append(p)
        else:
            if p not in d:
                d[p] = 2
            else:
                d[p] = d[p] + 1
    n.sort()
    #print (n)
    for j in n:
        if j not in d:
            print (j, "= 1")
        else:
            print (j, "=", d[j])
    

count_words(input())
