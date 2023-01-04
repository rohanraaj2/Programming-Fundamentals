n = int(input())
def pattern(n):
    s = ""
    j = ""
    for i in range(n):
        s += str((2 ** (i))) + " "
        if i > 0:
            j = str((2 ** (i - 1))) + " " + j
        print (s + j)
pattern(n)
