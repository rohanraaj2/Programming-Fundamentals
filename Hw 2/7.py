n = int(input())
def binary_string(n):
    s = ""
    if n == 0:
        return 0
    else:
        while n != 1 and n != 0 and n != -1:
            s = str(n % 2) + s
            n = int(n / 2)
        s = str(n) + s
        return s
print(binary_string(n))
