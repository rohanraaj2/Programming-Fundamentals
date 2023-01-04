n = int(input())
def pattern(n):
    s = ""
    for i in range (n):
        s = (str(2 ** i)) + " " + s
        print (s)
    
pattern(n)
