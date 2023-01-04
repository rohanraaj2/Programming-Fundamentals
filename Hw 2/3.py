a = int(input())
b = int(input())
def gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    if b > a:
        x = a
        y = b
        b = x
        a = y
    while b > 0:
        x = b
        y = a % b
        a = x
        b = y
    return a
            
print(gcd(a,b))
