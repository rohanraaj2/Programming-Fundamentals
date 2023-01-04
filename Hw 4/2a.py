def crossword_positions(puzzle):
    print (puzzle)
    y = []
    r = 0
    c = 0
    if type (puzzle) == str:
        for i in puzzle:
            l = []
            if i.isalpha() == True:
                l.append(i)
                l.append(r)
                l.append(c)
                c += 1
                y.append(l)
            else:
                r += 1
                c = 0
                continue
        return y
puzzle = eval(input())
print(crossword_positions(puzzle))
