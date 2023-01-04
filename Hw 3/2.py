n = int(input())
def cup(n):
    c = 0
    helper (n, c)
        
def helper (x, c):
    s = "*" + " "
    if x > 0:
        print ((" " * c) + (s * x))
        helper (x - 1, c + 1)

cup(n)
