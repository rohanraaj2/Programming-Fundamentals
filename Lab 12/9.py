# Enter your code here.
def get_positions(board, color):
    l = board.split()
    p = []
    if color not in board:
        return []
    else:
        for i in range(len(l)):
            if l[i] == color:
                t = (i // 3),
                t = t + (i % 3,)
                p.append(t)
        return p
board = input()
color = input()
print(get_positions(board, color))
