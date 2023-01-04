def special_sort(lst):
    if lst == []:
        return []
    #print (lst)
    if lst != []:
        x = lst[0][2]
        z = lst[0][2]
        y = []
        v = []
        q = []
        for i in range(len(lst)):
            if lst[i][2] < x:
                x = lst[i][2]
        for l in range(len(lst)):
            if lst[l][2] > z:
                z = lst[l][2]
        if type (x) == str and type (z) == str:
            x = int(x)
            z = int(z)
            for k in range(x, z + 1):
                for j in range(len(lst)):
                    if lst[j][2] == str(k):
                        y.append(lst[j])
                if y != []:
                    b = major(y)
            #print (b)
                    for s in b:
                        for t in s:
                    #print (t)
                            q.append(t)
                        #print (q)
                    
                y = []
            #return (v)
        elif type (x) == int and type (z) == int:
            for k in range(x, z + 1):
                for j in range(len(lst)):
                    if lst[j][2] == k:
                        y.append(lst[j])
                if y != []:
                    b = major(y)
            #print (b)
                    for s in b:
                        for t in s:
                        #print (t)
                            q.append(t)
                        #print (q)
                y = []
    #print ("hell", v[0][0][0])
        return (q)
        
def major(m):
    #print (m)
    a = []
    b = []
    c = []
    for p in range(len (m)):
        if m[p][1] not in a:
            a.append(m[p][1])
    a.sort()
    #print (a)
    for x in range (len(a)):
        for p in range(len (m)):
                if m[p][1] == a[x]:
                    b.append(m[p])
        #print (b)
        r = name(b)
        c.append(r)
        b = []
    #print (c)
    return (c)
    
def name (n):
    d = []
    h = []
    for e in range(len(n)):
        if n[e][0] not in d:
            d.append(n[e][0])
    d.sort()
    #print (d)
    for f in range (len(d)):
        for g in range(len (n)):
                if n[g][0] == d[f]:
                    h.append(n[g])
    #print (h)
    return (h)
        
print(special_sort(eval(input())))
