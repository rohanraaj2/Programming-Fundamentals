def compute_my_bill(lst):
    #x = []
    a = 0
    x = []
    y = []
    z = []
    for i in lst:
        i.append((i[1] * i[2]))
        x += i
    return x
print(compute_my_bill(eval(input())))
