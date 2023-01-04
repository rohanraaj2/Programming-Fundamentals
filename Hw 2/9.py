def bend(size):
    if size >= 2:
        print ("* " * size)
        l = (size * 2) - 2
        for i in range(0, l - 2, 2):
            print ("* " + (" " * i) + "* " + " " * (l - (i + 4)) + "*")
        print ("* " * size)
size = int(input())
bend(size)
