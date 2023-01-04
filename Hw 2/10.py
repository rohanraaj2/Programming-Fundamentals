def build_pyramid (b, c):
    y = 0
    k = 0
    for j in c:
        k += 1
    k -= 1
    if b < 0:
        
        l = int(-(b - 1) / 2)
        y = -b
        for i in range (0, l + 1):
            print ((" " * (i)) + (c * y) + (" " * (i)))
            print (" " * k * (i + 1), end = "")
            y -= 2
    else:
        import math
        l = math.ceil(b / 2)
        y += 1
        for i in range (l, 0, -1):
            print (" " * k * (i - 2), end = "")
            print ((" " * (i - 1)) + (c * y) + (" " * (i - 1)))
            y += 2
        
b = int(input())
c = input()
build_pyramid (b, c)
