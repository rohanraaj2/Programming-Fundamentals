# Enter your code here.
select = int(input())
n = int(input())

def prime_factors(num):
    s = []
    d = 2
    while num >= d:
        while num % d == 0:
            s.append(d)
            num = num // d
        d += 1
    return s
    
def special_numbers(num):
    s = 0
    x = []
    for i in range (num + 1):
        s = 0
        l = prime_factors(i)
        for j in l:
            s += j
        if i == s:
            x.append(s)
    return x
if select == 1:
    print(prime_factors(n))
elif select == 2:
   print (special_numbers(n))
