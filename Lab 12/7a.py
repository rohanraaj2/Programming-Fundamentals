def last_name_first(t):
    l = t[-1]
    x = []
    
    for i in t:
        k = i[-1],
        for j in range(len(i) - 1):
            k += i[j],
            #print (k)
        x.append(k)
    #for i in t:
        #print (i)
        #a = i[-1]
        #for j in range(len(i), 1, -1):
        #a = i[-1]
        #b = i[:len(i) - 1]
        #t = [a, b]
        #i = (i[-1],) + i[0:len(i) - 1]
        #l.append(i)
        #print (l)
    #t = l
    print (x)
#t = last_name_first(t)


t = eval(input())
last_name_first(t)
print(t)
