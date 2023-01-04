def crossword_positions(puzzle):
    #print (puzzle)
    y = []
    r = 0
    c = 0
    if type (puzzle) == str:
        for i in puzzle:
            l = []
            if (ord(i) > 32 and ord(i) < 127) or i == ' ':
                l.append(i)
                l.append(r)
                l.append(c)
                c += 1
                y.append(l)
            else:
                r += 1
                c = 0
            #print (r,c)
        return y
puzzle = eval(input())
print(crossword_positions(puzzle))
